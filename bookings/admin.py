from django.contrib import admin
from .models import TravelOption, Booking


@admin.register(TravelOption)
class TravelOptionAdmin(admin.ModelAdmin):
    list_display = ("id", "travel_type", "source", "destination", "depart_datetime", "price")
    list_filter = ("travel_type", "source", "destination")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "travel_option", "booking_date", "num_passengers", "total_price", "status")  
    # ✅ changed num_seats → num_passengers
    list_filter = ("status", "booking_date")
