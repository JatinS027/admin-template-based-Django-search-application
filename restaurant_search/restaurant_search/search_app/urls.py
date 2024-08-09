from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),  # Define your search URL here
    # Add other URLs specific to your app if needed
]
