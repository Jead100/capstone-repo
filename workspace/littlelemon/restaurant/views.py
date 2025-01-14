from django.shortcuts import render
from rest_framework import generics, viewsets
from datetime import datetime
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

def index(request):
    current_year = datetime.now().year
    return render(request, 'index.html', {'current_year': current_year})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer