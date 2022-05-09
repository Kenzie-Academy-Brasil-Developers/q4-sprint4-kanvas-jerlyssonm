from django.urls import path

from adresses.views import AddressView


urlpatterns = [
    path('address/', AddressView.as_view()),
]
