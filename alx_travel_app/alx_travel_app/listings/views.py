from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ListingSerializer, BookingSerializer
from .models import Listing, Booking



class ListingViewSet(viewsets.ModelViewSet):
    """
    Handles retrieving all listings
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewset(viewsets.ModelViewSet):
        queryset = Booking.objects.all()
        serializer_class = BookingSerializer
        