# # bookings/emails.py
# from django.core.mail import send_mail
# from django.conf import settings

# def send_booking_confirmation(booking):
#     """
#     Sends a simple confirmation email. Fails silently so it never breaks booking flow.
#     """
#     user = booking.user
#     if not user.email:
#         return

#     travel = booking.travel_option
#     subject = "Your booking is confirmed"
#     message = (
#         f"Hi {user.username},\n\n"
#         f"Your booking is confirmed!\n\n"
#         f"Trip: {travel.source} → {travel.destination}\n"
#         f"Departure: {travel.depart_datetime}\n"
#         f"Seats: {booking.num_passengers}\n"
#         f"Total: ₹{booking.total_price}\n\n"
#         f"Booking ID: {booking.id}\n"
#         f"Thanks for booking with us!"
#     )

#     send_mail(
#         subject=subject,
#         message=message,
#         from_email=getattr(settings, "DEFAULT_FROM_EMAIL", None),
#         recipient_list=[user.email],
#         fail_silently=True,
#     )
# bookings/emails.py
from django.core.mail import send_mail
from django.conf import settings

def send_booking_confirmation(booking):
    """
    Sends a simple confirmation email. Fails silently so it never breaks booking flow.
    """
    user = booking.user
    if not user.email:
        return

    travel = booking.travel_option
    subject = "Your booking is confirmed"
    message = (
        f"Hi {user.username},\n\n"
        f"Your booking is confirmed!\n\n"
        f"Trip: {travel.source} → {travel.destination}\n"
        f"Departure: {travel.depart_datetime}\n"
        f"Seats: {booking.num_passengers}\n"
        f"Total: ₹{booking.total_price}\n\n"
        f"Booking ID: {booking.id}\n"
        f"Thanks for booking with us!"
    )

    # ---------------- DEBUG ADDITION ----------------
    print("📧 Sending email to:", user.email)  # this will show in your console
    # temporarily fail loudly to catch errors
    send_mail(
        subject=subject,
        message=message,
        from_email=getattr(settings, "DEFAULT_FROM_EMAIL", None),
        recipient_list=[user.email],
        fail_silently=False,  # change True -> False temporarily
    )
