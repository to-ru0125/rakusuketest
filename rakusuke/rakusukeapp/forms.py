from .models import RakusukeSchedule
from .models import RakusukeSubject
from .models import RakusukeFixed
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

FIELD_NAME_MAPPING = {
        'schedule_do':'schedule_do_0',
        'schedule_category':'schedule_category_0',
        'schedule_worktime':'schedule_worktime_0',
        'schedule_priority':'schedule_priority_0',
}

FIXED_FORM_MAPPING = {
        'fixed_adaptation': 'fixed_adaptation_0'
}

class ScheduleCreateForm(forms.ModelForm):
    class Meta:
        model = RakusukeSchedule
        fields = ('schedule_do',
                  'schedule_category',
                  'schedule_worktime',
                  'schedule_priority',
        )
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

        def form_valid(self, form):
            histories = form.save(commit=False)
            histories.user = self.request.user
            histories.save()
            messages.success(self.request, '作成しました。')
            return super().form_valid(form)

        def add_prefix(self, field_name):
            field_name = FIELD_NAME_MAPPING.get(field_name, field_name)
            return super(ScheduleCreateForm, self).add_prefix(field_name)


class SubjectCreateForm(forms.ModelForm):
    class Meta:
        model = RakusukeSubject
        fields = ('subject_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class FixedScheduleForm(forms.ModelForm):
    class Meta:
        model = RakusukeFixed
        fields =('user',
                 'fixed_do',
                 'fixed_start_time',
                 'fixed_end_time',
                 'fixed_adaptation')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

        def form_valid(self, form):
            histories = form.save(commit=False)
            histories.user = self.request.user
            histories.save()
            messages.success(self.request, '作成しました。')
            return super().form_valid(form)

        def add_prefix(self, field_name):
            field_name = FIXED_FORM_MAPPING.get(field_name, field_name)
            return super(FixedScheduleForm, self).add_prefix(field_name)
