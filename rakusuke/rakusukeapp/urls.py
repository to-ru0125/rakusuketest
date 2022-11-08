from django.urls import path

from . import views

app_name= 'rakusukeapp'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('onedayschedulelist/',views.OnedayschedulelistView.as_view(),name="onedayschedulelist"),
    path('oneweekschedulelist/',views.OneweekschedulelistView.as_view(),name="oneweekschedulelist"),
    path('makeschedule/',views.CreateView.as_view(),name="makescheduleview"),
]
