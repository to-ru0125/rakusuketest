from .models import RakusukeSchedule
from django import forms

class ScheduleCreateForm(forms.ModelForm):
    class Meta:
        model = RakusukeSchedule
        fields = ('schedule_priority',
                  'schedule_start_date',
                  'schedule_end_date',
                  'schedule_worktime',
                  'sucedule_creation_stage',
                  'sucedule_ditching')
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'