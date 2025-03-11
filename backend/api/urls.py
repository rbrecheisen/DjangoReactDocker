from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ItemList

urlpatterns = [
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('items/', ItemList.as_view(), name='item-list'),
]
