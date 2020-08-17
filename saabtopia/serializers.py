from rest_framework import serializers
from .models import Producent, Car, UserCar, Place
from django.contrib.auth import get_user_model




class AdminProducentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producent
        fields = [
            'id',
            'name',
            'slug',
            'user',
            'image_url',
            'description',
            # 'url',
        ]

        lookup_field = 'slug'
        extra_kwargs = {'url': {'lookup_field': 'slug'}}


class ProducentSerializer(AdminProducentSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class AdminCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'id',
            'name',
            'producent',
            'production',
            'car_class',
            'body_style',
            'engine',
            'transmission',
            'airconditioning',
            'length',
            'width',
            'height',
            'user',
            'description',
            # 'url',
        ]


class CarSerializer(AdminCarSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    # pole przyjmie wartosc aktualnie zalogowanego usera


class AdminPlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = [
            'id',
            'name',
            'user',
            'description',
            # 'url',
        ]


class PlaceSerializer(AdminPlaceSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class AdminUserCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCar
        fields = [
            'id',
            'name',
            'description',
            'place',
            'car',
            'date_come',
            'user',
            'image_url',
            'description',
            # 'url',
        ]


class UserCarSerializer(AdminUserCarSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'email',
            'password',
        ]