from django.contrib import admin
from .models import Producent, Car, Place, UserCar


class CarsInline(admin.StackedInline):
    model = Car
    extra = 0

# Register your models here.


class CarAdmin(admin.ModelAdmin):

    list_display = ('name', 'producent',
    'engine', 'transmission', 'airconditioning', 'length', 'width',
    'height', 'description' )
    def krotki_opis(self, obj):
        return (
            f'{obj.description[:50]}...'
            if len(obj.description) > 50
            else obj.description
        )


class ProducentAdmin (admin.ModelAdmin):
    list_display = ('name', 'user', 'description')
    def krotki_opis(self, obj):
        return (
            f'{obj.description[:50]}...'
            if len(obj.description) > 50
            else obj.description
        )


class PlaceAdmin (admin.ModelAdmin):

    list_display = ('name', 'user', 'openair', 'description' )
    def krotki_opis(self, obj):
        return (
            f'{obj.description[:50]}...'
            if len(obj.description) > 50
            else obj.description
        )


class UserCarsAdmin (admin.ModelAdmin):

    list_display = ('name', 'user', 'description', 'date_come' , 'place'
     )

    def krotki_opis(self, obj):
        return (
            f'{obj.description[:50]}...'
            if len(obj.description) > 50
            else obj.description
        )



# Register your models here.


admin.site.register(Car, CarAdmin)
admin.site.register(UserCar, UserCarsAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Producent, ProducentAdmin)
