from django.db import models
from django.contrib.auth.models import User


class TravelOption(models.Model):
    TRAVEL_TYPES = [
        ("Flight", "Flight"),
        ("Train", "Train"),
        ("Bus", "Bus"),
    ]
    available_seats = models.IntegerField(default=0)
    travel_type = models.CharField(max_length=20, choices=TRAVEL_TYPES)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    depart_datetime = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.travel_type}: {self.source} → {self.destination} ({self.depart_datetime})"


class Booking(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    num_passengers = models.PositiveIntegerField(default=1)

    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")

    def __str__(self):
        return f"Booking {self.id} - {self.user.username} - {self.status}"
