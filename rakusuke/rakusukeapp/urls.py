from django.urls import path

from . import views

app_name= 'rakusukeapp'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('onedayschedulelist/',views.OnedayschedulelistView.as_view(),name="onedayschedulelist"),
    path('oneweekschedulelist/',views.OneweekschedulelistView.as_view(),name="oneweekschedulelist"),
    path('calendar/',views.CalendarView.as_view(),name="calendar"),
    path('calendar/<int:year>/<int:month>/',views.CalendarView.as_view(),name="calendar"),
    # path('fixedschedule/',views.FixedscheduleView.as_view(),name="fixedschedule"),
    path('fixed_create/',views.FixedCreateView.as_view(),name="fixed_create"),
    path('fixed_list/',views.FixedListView.as_view(),name="fixed_list"),
    path('fixed_detail/<int:pk>/',views.FixedDetailView.as_view(),name="fixed_detail"),
    path('makeschedule/',views.MakescheduleView.as_view(),name="makeschedule"),
    path('calendar-detail/<int:year>/<int:month>/<int:day>/',views.CalendarDetailView.as_view(),name="calendardetail"),
    path('subjectlist/',views.SubjectListView.as_view(),name="subjectlist"),
    path('subjectupdate/',views.SubjectUpdateView.as_view(),name="subjectupdate"),
    path('subjectcreate/',views.SubjectCreateView.as_view(),name="subjectcreate"),
    path('detaillist/',views.DetailListView.as_view(),name="detaillist"),
    path('subjectcreate/',views.SubjectCreateView.as_view(),name="subjectcreate"),
    # path('calender-detail/<int:pk>',views.CalendarDetailView.as_view(),name="calender_detail")
]
