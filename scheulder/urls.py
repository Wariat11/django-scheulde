from django.urls import path
from .views import (
    CalendarView,
    EventCreateView,
    EventDetailView,
    EventUpdateView,
    EventDeleteView,
)

app_name = 'calendar'
urlpatterns = [
    path("", CalendarView.as_view(), name='scheulder'),
    path("add/", EventCreateView.as_view(), name='add'),
    path("<int:pk>/detail", EventDetailView.as_view(), name='detail'),
    path("<int:pk>/update", EventUpdateView.as_view(), name='update'),
    path("<int:pk>/delete", EventDeleteView.as_view(), name='delete'),
]
