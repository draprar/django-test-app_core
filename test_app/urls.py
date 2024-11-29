from django.urls import path
from .views import driving_test

urlpatterns = [
    path('', driving_test, name='driving_test'),
]
            