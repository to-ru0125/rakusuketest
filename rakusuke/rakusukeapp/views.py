from django.views import generic
from .models import RakusukeSchedule
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ScheduleCreateForm

class IndexView(generic.TemplateView):
    template_name = "index.html"

class OnedayschedulelistView(generic.TemplateView,LoginRequiredMixin):
    template_name = "onedayschedulelist.html"

class OneweekschedulelistView(generic.TemplateView,LoginRequiredMixin):
    template_name = "oneweekschedulelist.html"

class CalendarView(generic.TemplateView,LoginRequiredMixin):
    model = RakusukeSchedule
    template_name = "calendar.html"

class FixedscheduleView(generic.TemplateView):
    template_name = "fixedschedule.html"

# class MakescheduleView(generic.TemplateView):
#     template_name = 'makeschedule.html'

class MakescheduleView(LoginRequiredMixin,generic.FormView):
    model = RakusukeSchedule
    template_name = 'makeschedule.html'
    form_class = ScheduleCreateForm
    success_url = reverse_lazy('成功後ページ')

    def form_valid(self, form):
        histories = form.save(commit=False)
        histories.user = self.request.user
        histories.save()
        messages.success(self.request, '投稿しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "投稿に失敗しました。")
        return super().form_invalid(form)
