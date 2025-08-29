# bookings/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import TravelOption, Booking
from django.urls import reverse
from django.utils import timezone
from decimal import Decimal
from datetime import timedelta

class BookingTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='pass')
        self.travel = TravelOption.objects.create(
            travel_type='bus',
            provider='TestBus',
            source='A',
            destination='B',
            depart_datetime=timezone.now() + timedelta(days=1),
            price=Decimal('100.00'),
            available_seats=10
        )

    def test_booking_creates_and_decrements_seats(self):
        self.client.login(username='test', password='pass')
        resp = self.client.post(reverse('book_travel', args=[self.travel.pk]), {'num_seats': 2})
        self.assertRedirects(resp, reverse('my_bookings'))
        self.travel.refresh_from_db()
        self.assertEqual(self.travel.available_seats, 8)
        booking = Booking.objects.get(user=self.user)
        self.assertEqual(booking.num_seats, 2)
        self.assertEqual(booking.total_price, Decimal('200.00'))
