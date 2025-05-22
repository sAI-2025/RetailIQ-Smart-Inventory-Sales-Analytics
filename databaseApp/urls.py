from django.urls import path
from . import views

urlpatterns = [
    path('add_random_values/', views.add_randomvalues, name='add_randomvalues'),
    path('count/', views.total_rows, name='count'),
    path('live-values/', views.live_values, name='live_values'),  # Show live values
]

