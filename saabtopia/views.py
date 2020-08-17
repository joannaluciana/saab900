from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView

from .models import Producent, Car, Place, UserCar
from .serializers import (
     AdminProducentSerializer,
     ProducentSerializer,
     AdminCarSerializer,
     CarSerializer,
     AdminPlaceSerializer,
     PlaceSerializer,
     AdminUserCarSerializer,
     UserCarSerializer,
     UserSerializer,
     )


class ProducentViewSet(viewsets.ModelViewSet):
    queryset = Producent.objects.all()
    serializer_class = ProducentSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class UserCarViewSet(viewsets.ModelViewSet):
    queryset = UserCar.objects.all()
    serializer_class = UserCarSerializer