from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.TemplateView):
    template_name = "index.html"

class OnedayschedulelistView(generic.TemplateView,LoginRequiredMixin):
    template_name = "onedayschedulelist.html"

class OneweekschedulelistView(generic.TemplateView,LoginRequiredMixin):
    template_name = "oneweekschedulelist.html"

class CalendarView(generic.TemplateView,LoginRequiredMixin):
    template_name = "calendar.html"