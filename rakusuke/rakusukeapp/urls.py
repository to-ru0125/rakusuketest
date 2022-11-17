from django.urls import path

from . import views

app_name= 'rakusukeapp'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('onedayschedulelist/',views.OnedayschedulelistView.as_view(),name="onedayschedulelist"),
    path('oneweekschedulelist/',views.OneweekschedulelistView.as_view(),name="oneweekschedulelist"),
    path('calendar/<int:year>/<int:month>/',views.CalendarView.as_view(),name="calendar"),
    path('fixedschedule/',views.FixedscheduleView.as_view(),name="fixedschedule"),
    path('makeschedule/',views.MakescheduleView.as_view(),name="makeschedule"),
]
