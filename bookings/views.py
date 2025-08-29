from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.utils import timezone
from .models import TravelOption, Booking
from .forms import SignUpForm, ProfileForm, BookingForm
from django.core.paginator import Paginator
from django.db.models import Q
from .emails import send_booking_confirmation


def home(request):
    return render(request, 'home.html')


def travel_list(request):
    q_type = request.GET.get('type')
    q_src = request.GET.get('source')
    q_dest = request.GET.get('destination')
    q_date = request.GET.get('date')

    qs = TravelOption.objects.filter(depart_datetime__gte=timezone.now())

    if q_type:
        qs = qs.filter(travel_type=q_type)
    if q_src:
        qs = qs.filter(source__icontains=q_src)
    if q_dest:
        qs = qs.filter(destination__icontains=q_dest)
    if q_date:
        qs = qs.filter(depart_datetime__date=q_date)

    # Search across fields
    search = request.GET.get('search')
    if search:
        qs = qs.filter(
            Q(source__icontains=search) |
            Q(destination__icontains=search) |
            Q(provider__icontains=search)
        )

    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    travel_options = paginator.get_page(page)

    return render(request, 'travel_list.html', {'travel_options': travel_options})


def travel_detail(request, pk):
    travel = get_object_or_404(TravelOption, pk=pk)
    return render(request, 'travel_detail.html', {'travel': travel})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created. Welcome!")
            return redirect('travel_list')
        else:
            # Print errors in console for debugging
            print("Signup form errors:", form.errors)
            messages.error(request, "Please fix the errors below.")
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})


@login_required
@transaction.atomic
def book_travel(request, pk):
    travel = get_object_or_404(TravelOption, pk=pk)

    if request.method == "POST":
        num_passengers = int(request.POST.get("num_passengers", 1))

        # Validate seat availability
        if num_passengers > travel.available_seats:
            messages.error(request, f"Only {travel.available_seats} seats available!")
            return redirect("book_travel", pk=pk)

        total_price = travel.price * num_passengers

        # Create booking
        booking = Booking.objects.create(
            user=request.user,
            travel_option=travel,
            num_passengers=num_passengers,  # ✅ correct field
            total_price=total_price,
            status="Confirmed"
        )

        # Update available seats
        travel.available_seats -= num_passengers
        travel.save()

        # Send confirmation email
        send_booking_confirmation(booking)

        messages.success(request, "Booking confirmed! A confirmation email has been sent.")
        return redirect("my_bookings")

    return render(request, "book_travel.html", {"travel": travel})


@login_required
def my_bookings(request):
    bookings = request.user.booking_set.select_related('travel_option').order_by('-booking_date')
    return render(request, 'my_bookings.html', {'bookings': bookings})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)  # ✅ use id

    if booking.status == "Cancelled":  # ✅ must match model choice
        messages.info(request, "Booking already cancelled.")
    else:
        travel = booking.travel_option
        travel.available_seats += booking.num_passengers  # ✅ correct field
        travel.save()
        booking.status = "Cancelled"
        booking.save()
        messages.success(request, f"Booking {booking_id} cancelled.")

    return redirect('my_bookings')
