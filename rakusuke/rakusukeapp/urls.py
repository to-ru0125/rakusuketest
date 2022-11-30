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
    # path('fixed_update/<int:pk>/', views.FixedUpdetaView.as_view(), name="fixed_update"),
    path('fixed_delete/<int:pk>/',views.FixedDeleteView.as_view(),name="fixed_delete"),
    path('makeschedule/',views.MakescheduleView.as_view(),name="makeschedule"),
    path('calendar-detail/<int:year>/<int:month>/<int:day>/',views.CalendarDetailView.as_view(),name="calendardetail"),
    path('subjectlist/',views.SubjectListView.as_view(),name="subjectlist"),
    path('detaillist/<int:pk>/',views.DetailListView.as_view(),name="detaillist"),
    path('subjectupdate/',views.SubjectUpdateView.as_view(),name="subjectupdate"),
    path('detailupdate/<int:pk>/',views.DetailUpdateView.as_view(),name="detailupdate"),
    path('subjectcreate/',views.SubjectCreateView.as_view(),name="subjectcreate"),
    path('detailcreate/<int:subject_id_id>/',views.DetailCreateView.as_view(),name="detailcreate"),
    path('subjectdelete/<int:pk>',views.SubjectDeleteView.as_view(),name='subjectdelete'),
    # path('tentative_schedule/<int:date>/', views.TentativeScheduleView.as_view(),
    #      name="tentativeschedule")
    # path('calender-detail/<int:pk>',views.CalendarDetailView.as_view(),name="calender_detail")
]
