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

    lookup_field = "slug"

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            # self.lookup_field='pk'
            return AdminProducentSerializer
        return ProducentSerializer

    def get_queryset(self) :
        if self.request.user.is_superuser:
            return Producent.objects.all()
        return Producent.objects.filter(user=self.request.user)

class CarViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return AdminCarSerializer
        return CarSerializer

    def get_queryset(self):
        if self.request.user.is_superuser :
            return Car.objects.all()
        return Car.objects.filter(user=self.request.user)

class PlaceViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return AdminPlaceSerializer
        return PlaceSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Place.objects.all()
        return Place.objects.filter(user=self.request.user)

class UserCarViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return AdminUserCarSerializer
        return UserCarSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return UserCar.objects.all()
        return UserCar.objects.filter(user=self.request.user)


class ProfileRetrieveView(RetrieveAPIView):

    def retrieve(self, request, pk = None):
        User = get_user_model()
        serializer = UserSerializer(User.objects.get(pk=request.user.pk))
        return Response(serializer.data)
