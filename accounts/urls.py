from django.urls import path
from .views import  AccountsView, login_user_view


urlpatterns = [
    path('accounts/', AccountsView.as_view()),
    path('login/', login_user_view),
]
