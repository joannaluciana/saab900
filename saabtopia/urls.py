from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('producent', views.ProducentViewSet, basename='producents')
router.register('cars', views.CarViewSet, basename='car')
router.register('places', views.PlaceViewSet, basename='place')
router.register('usercars', views.UserCarViewSet, basename='usercars')
# router.register('account', views.AccountViewSet, basename='account')


urlpatterns = [
    path('profile/', views.ProfileRetrieveView.as_view(), name='profile'),
    path('', include(router.urls)),
]