from .models import RakusukeSchedule
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