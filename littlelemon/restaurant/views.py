from django.shortcuts import render
from rest_framework import viewsets,generics
from django.contrib.auth.models import User
from .models import Menu,Booking
from .serializers import UserSerializer,MenuSerializer,BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer