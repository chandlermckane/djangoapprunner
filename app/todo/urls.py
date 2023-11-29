from django.urls import path
from .views import (
    ListView,
    ListDetailView,
    ListCreateView,
    ListUpdateView,
    ListDeleteView,
    UserListsView,
    AnnouncementsView,
  
)
from . import views


urlpatterns = [
    path('', ListView.as_view(), name='todo-home'),
    path('user/<str:username>', UserListsView.as_view(), name='user-lists'),
    path('list/<int:pk>/', ListDetailView.as_view(), name='list-detail'),
    path('list/new/', ListCreateView.as_view(), name='list-create'),
    path('list/<int:pk>/update/', ListUpdateView.as_view(), name='list-update'),
    path('list/<int:pk>/delete/', ListDeleteView.as_view(), name='list-delete'),
    path('about/', views.about, name='todo-about'),
    path('announcements/<int:pk>/', AnnouncementsView.as_view(), name='announcements'),
    path('feedback/<int:pk>', views.FeedbackView.as_view(), name='feedback'), 
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    ]