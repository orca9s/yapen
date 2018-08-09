from django.urls import path


from reservation.views import ReservationRoom

urlpatterns = [
    path('<int:pk>/',
         ReservationRoom.as_view(),
         name='Reservation'),
    path('<int:pk>/<str:date>/',
         ReservationRoom.as_view(),
         name='Reservation'),
]