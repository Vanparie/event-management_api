from django.urls import path, include
from .views import EventListCreateAPIView

urlpatterns = [
    path('events/', EventListCreateAPIView.as_view(), name='event-list-create'),
]
