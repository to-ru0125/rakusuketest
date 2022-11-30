from django.views import generic
from .models import RakusukeSchedule
from .models import RakusukeDetail
from .models import RakusukeSubject
from .models import RakusukeFixed
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ScheduleCreateForm
from .forms import SubjectCreateForm
from .forms import DetailCreateForm
from .forms import FixedScheduleForm
import calendar
from collections import deque
import datetime
import webbrowser
from django.shortcuts import redirect, render
from django.http import HttpResponse
import re
from django.db.models import Prefetch
from . import models
class BaseCalendarMixin:
    """カレンダー関連Mixinの、基底クラス"""
    first_weekday = 6  # 0は月曜から、1は火曜から。6なら日曜日からになります。お望みなら、継承したビューで指定してください。
    week_names = ['月', '火', '水', '木', '金', '土', '日']  # これは、月曜日から書くことを想定します。['Mon', 'Tue'...

    def setup_calendar(self):
        """内部カレンダーの設定処理

        calendar.Calendarクラスの機能を利用するため、インスタンス化します。
        Calendarクラスのmonthdatescalendarメソッドを利用していますが、デフォルトが月曜日からで、
        火曜日から表示したい(first_weekday=1)、といったケースに対応するためのセットアップ処理です。

        """
        self._calendar = calendar.Calendar(self.first_weekday)

    def get_week_names(self):
        """first_weekday(最初に表示される曜日)にあわせて、week_namesをシフトする"""
        week_names = deque(self.week_names)
        week_names.rotate(-self.first_weekday)  # リスト内の要素を右に1つずつ移動...なんてときは、dequeを使うと中々面白いです
        return week_names


class MonthCalendarMixin(BaseCalendarMixin):
    # カレンダー機能
    #     月間カレンダーの機能を提供するMixin

    def get_previous_month(self, date):
        # 前月を返す
        if date.month == 1:
            return date.replace(year=date.year - 1, month=12, day=1)
        else:
            return date.replace(month=date.month - 1, day=1)

    def get_next_month(self, date):
        # 次月を返す
        if date.month == 12:
            return date.replace(year=date.year + 1, month=1, day=1)
        else:
            return date.replace(month=date.month + 1, day=1)

    def get_now_month(self, date):
        # 今月を返す
        if date.month == 12:
            return date.replace(year=date.year)
        else:
            return date.replace(month=date.month)

    def get_month_days(self, date):
        # yearが0の場合今の年月とする
        if date.year == "":
            date.year = datetime.year
            date.month = datetime.month
        # その月の全ての日を返す
        return self._calendar.monthdatescalendar(date.year, date.month)

    def get_current_month(self):
        # 現在の月を返す
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        if month and year:
            month = datetime.date(year=int(year), month=int(month), day=1)
        else:
            month = datetime.date.today().replace(day=1)
        return month

    def get_month_calendar(self):
        # 月間カレンダー情報の入った辞書を返す
        self.setup_calendar()
        current_month = self.get_current_month()
        calendar_data = {
            'now': datetime.date.today(),
            'month_days': self.get_month_days(current_month),
            'month_current': current_month,
            'month_previous': self.get_previous_month(current_month),
            'month_next': self.get_next_month(current_month),
            'month_now': self.get_now_month(current_month),
            'week_names': self.get_week_names(),
        }
        return calendar_data


class CalendarDetailView(LoginRequiredMixin, generic.DetailView):
    model = RakusukeDetail
    template_name = 'calendar_datail.html'


class CalendarView(MonthCalendarMixin, generic.TemplateView, LoginRequiredMixin):
    """月間カレンダーを表示するビュー"""
    template_name = "calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class IndexView(generic.TemplateView):
    # ホーム画面表示
    template_name = "index.html"


class OnedayschedulelistView(generic.TemplateView, LoginRequiredMixin):
    # 一日のスケジュール表示
    template_name = "onedayschedulelist.html"


class OneweekschedulelistView(generic.TemplateView, LoginRequiredMixin):
    # 週のスケジュール表示
    template_name = "oneweekschedulelist.html"


# class AAAACalendarView(generic.TemplateView,LoginRequiredMixin):
#     # カレンダー表示
#     model = RakusukeSchedule
#     template_name = "calendar.html"


# class FixedscheduleView(LoginRequiredMixin,generic.FormView,generic.ListView):
#     model = RakusukeFixed
#     template_name = 'fixedschedule.html'
#     form_class = FixedScheduleForm
#     success_url = reverse_lazy('成功後ページ')
#
#     def post(self, request, *args, **kwargs):
#         context = {
#             'fixed_do': request.POST['fixed_do'],
#             'fixed_start_time': request.POST['fixed_start_time'],
#             'fixed_end_time': request.POST['fixed_end_time'],
#
#         }
#         return render(request, 'fixedschedule.html', context)
#
#     def form_valid(self, form):
#         histories = form.save(commit=False)
#         histories.user = self.request.user
#         histories.save()
#         messages.success(self.request, '作成しました。')
#         return super().form_valid(form)
#
#     def form_invalid(self, form):
#         messages.error(self.request, "作成に失敗しました。")
#         return super().form_invalid(form)


class MakescheduleView(LoginRequiredMixin, generic.CreateView):
    # スケジュール作成画面表示
    model = RakusukeSchedule
    template_name = 'makeschedule.html'
    form_class = ScheduleCreateForm

    def post(self, request, *args, **kwrgs):
        dateList = []
        doList = []
        categoryList = []
        priorityList = []
        worktimeList = []

        for i in request.POST.items():
            if re.match(r'schedule_date_0', i[0]):
                dateList.append(i[1])
            if re.match(r'schedule_do_*', i[0]):
                doList.append(i[1])
            if re.match(r'schedule_category_*', i[0]):
                categoryList.append(i[1])
            if re.match(r'schedule_priority_*', i[0]):
                priorityList.append(i[1])
            if re.match(r'schedule_worktime_*', i[0]):
                worktimeList.append(i[1])

        for i in range(len(doList)):
            rakusukeschedule = RakusukeSchedule.objects.create(
                schedule_date=dateList[i],
                schedule_do=doList[i],
                schedule_category=categoryList[i],
                schedule_priority=priorityList[i],
                schedule_worktime=worktimeList[i],
                user=self.request.user,
            )
            rakusukeschedule.save()

        def form_invalid(self, form):
            messages.error(self.request, "作成に失敗しました。")
            return super().form_invalid(form)


class SubjectListView(LoginRequiredMixin, generic.ListView):
    # 科目一覧画面表示
    template_name = 'subjectlist.html'
    model = RakusukeSubject

    def get_queryset(self):
        diaries = RakusukeSubject.objects.filter(user=self.request.user)
        return diaries

class DetailListView(LoginRequiredMixin, generic.ListView):
    # 科目一覧画面表示
    template_name = 'detaillist.html'
    model = RakusukeDetail

    def get_context_data(self, **kwargs):
        context = super(DetailListView, self).get_context_data(**kwargs)
        context['rakusukedetail'] = RakusukeDetail.objects.filter(user=self.request.user, subject_id=self.kwargs['pk'])
        context['detailpk'] = RakusukeSubject.objects.filter(id=self.kwargs['pk'])
        return context


class SubjectCreateView(LoginRequiredMixin, generic.CreateView):
    # 科目追加
    template_name = 'subjectcreate.html'
    form_class = SubjectCreateForm
    success_url = reverse_lazy('rakusukeapp:subjectlist')

    def form_valid(self, form):
        rakusukeapp = form.save(commit=False)
        rakusukeapp.user = self.request.user
        rakusukeapp.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class DetailCreateView(LoginRequiredMixin, generic.CreateView):
    # 科目追加
    template_name = 'detailcreate.html'
    form_class = DetailCreateForm
    success_url = reverse_lazy('rakusukeapp:subjectlist' )

    def form_valid(self, form):
        rakusukeapp = form.save(commit=False)
        rakusukeapp.user = self.request.user
        rakusukeapp.subject_id = RakusukeSubject.objects.get(id=self.kwargs.get('subject_id_id'))
        rakusukeapp.detail_achieved = 0
        rakusukeapp.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class SubjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'subjectcreate.html'
    model = RakusukeSubject
    fields = '__all__'
    success_url = reverse_lazy('rakusukeapp:index')


class DetailUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'detaillist.html'
    model = RakusukeDetail
    success_url = reverse_lazy('rakusukeapp:index')
    form_class = DetailCreateForm

    def get_success_url(self):
        fields = RakusukeDetail.objects.filter(user=self.request.user, subject_id=self.kwargs['pk'])
        return reverse_lazy('rakusukeapp:detaillist')

    def form_valid(self, form):
        messages.success(self.request, '日記を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の更新に失敗しました。")
        return super().form_invalid(form)


class SubjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'subjectdelete.html'
    model = RakusukeSubject
    success_url = reverse_lazy('rakusukeapp:subjectlist')

class TentativeScheduleView(LoginRequiredMixin,generic.ListView):
    model = RakusukeSchedule
    template_name = 'tentative_schedule.html'
    field = model.objects.latest('created_at')
    fields = model.objects.filter(schedule_date=field.schedule_date)

class FixedCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'fixed_create.html'
    form_class = FixedScheduleForm
    success_url = reverse_lazy('rakusukeapp:fixed_list')

    def post(self, request, *args, **kwrgs):
        doList = []
        startTimeList = []
        endTimeList = []
        adaptationList = []

        for i in request.POST.items():
            if re.match(r'fixed_do_*', i[0]):
                doList.append(i[1])
            if re.match(r'fixed_start_time_*', i[0]):
                startTimeList.append(i[1])
            if re.match(r'fixed_end_time_*', i[0]):
                endTimeList.append(i[1])
            if re.match(r'fixed_adaptation_*', i[0]):
                adaptationList.append(i[1])

        for i in range(len(doList)):
            fixedschedule = RakusukeFixed.objects.create(
                fixed_do=doList[i],
                fixed_start_time=startTimeList[i],
                fixed_end_time=endTimeList[i],
                fixed_adaptation=adaptationList[i],
                user=self.request.user,
            )
            fixedschedule.save()
            return redirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, "固定スケジュールの作成に失敗しました")
        return super().form_valid(form)

class FixedListView(LoginRequiredMixin, generic.ListView):
    model = RakusukeFixed
    template_name = 'fixed_list.html'
    # 一つのページに何個こてすけを表示するか設定
    paginate_by = 50

    def get_queryset(self):
        diaries = RakusukeFixed.objects.filter(user=self.request.user).order_by('-fixed_start_time')
        return diaries

class FixedDetailView(LoginRequiredMixin, generic.DetailView):
    model = RakusukeFixed
    template_name = 'fixed_detail.html'

class FixedDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = RakusukeFixed
    template_name = 'fixed_delete.html'
    success_url = reverse_lazy('rakusukeapp:fixed_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "固定スケジュールを削除しました")
        return super().delete(request, *args, **kwargs)

class FixedUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = RakusukeFixed
    template_name = 'fixed_update.html'
    form_class = FixedScheduleForm

    def get_success_url(self):
        return reverse_lazy('rakusukeapp:fixed_detail', kwargs={'pk': self.kwargs['pk']})

    def form_invalid(self, form):
        messages.success(self.request, "固定スケジュールを更新しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "固定スケジュールの更新に失敗しました")
        return super().form_valid(form)
