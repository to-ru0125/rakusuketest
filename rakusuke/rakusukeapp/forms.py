from .models import RakusukeSchedule
from .models import RakusukeSubject
from .models import RakusukeFixed
from django import forms

class ScheduleCreateForm(forms.ModelForm):
    class Meta:
        model = RakusukeSchedule
        fields = ('schedule_do',
                  'schedule_category',
                  'schedule_worktime',
                  'schedule_priority',
                  'schedule_ditching')
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

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
        fields =('fixed_do',
                 'fixed_start_time',
                 'fixed_end_time',
                 'fixed_adaptation')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'