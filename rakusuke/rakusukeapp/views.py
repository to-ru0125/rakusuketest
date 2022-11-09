from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.TemplateView):
    template_name = "index.html"

class OnedayschedulelistView(generic.TemplateView,LoginRequiredMixin):
    template_name = "onedayschedulelist.html"

class OneweekschedulelistView(generic.TemplateView,LoginRequiredMixin):
    template_name = "oneweekschedulelist.html"

class CalendarView(generic.TemplateView,LoginRequiredMixin):
    # model = RakusukeSchedule
    template_name = "calendar.html"

    # def get_queryset(self):
    #     diaries = Shopping.objects.filter(user=self.request.user).order_by('-created_at')
    #     return diaries
    #
    # def get_queryset(self):
    #     q_word = self.request.GET.get('query')
    #
    #     if q_word:
    #         diaries = Shopping.objects.filter((Q(product1__icontains=q_word) | Q(product2__icontains=q_word) | Q(product3__icontains=q_word) | Q(product4__icontains=q_word) | Q(product5__icontains=q_word) | Q(product6__icontains=q_word)), user = self.request.user).order_by('-created_at')
    #         return diaries
    #     else:
    #         diaries = Shopping.objects.filter(user=self.request.user).order_by('-created_at')
    #         return diaries