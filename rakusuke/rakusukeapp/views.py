from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import RakusukeSchedule
from .forms import ScheduleCreateForm

class IndexView(generic.TemplateView):
    template_name = "index.html"

class CreateView(LoginRequiredMixin,generic.FormView):
    model = RakusukeSchedule
    template_name = 'make_schedule.html'
    form_class = ScheduleCreateForm
    success_url = reverse_lazy('成功後ページ')

    def form_valid(self, form):
        schedule = form.save(commit=False)
        schedule.user = self.request.user
        schedule.save()
        messages.success(self.request, '投稿しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "投稿に失敗しました。")
        return super().form_invalid(form)

class OnedayschedulelistView(generic.TemplateView):
    template_name = "onedayschedulelist.html"

class OneweekschedulelistView(generic.TemplateView):
    template_name = "oneweekschedulelist.html"