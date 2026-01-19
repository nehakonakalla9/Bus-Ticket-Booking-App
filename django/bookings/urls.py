from django.urls import path
from .views import RegisterView, LoginView, BusListCreateView, UserBookingView, BookingView, BusDetailView

urlpatterns = [
    path('buses/', BusListCreateView.as_view(), name='buslist'), #get
    path('buses/<int:pk>/', BusDetailView.as_view(), name='bus-detail'), #post
    path('register/', RegisterView.as_view(), name = 'register'), #post
    path('login/', LoginView.as_view(), name = 'login'), #post
    path('user/<int:user_id>/bookings/', UserBookingView.as_view(), name="user-bookings"), #get
    path('booking/', BookingView.as_view(), name="booking") #post
]