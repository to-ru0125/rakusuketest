from accounts.models import CustomUser
from django.db import models


class rakusuke_schedule(models.Model):
    user_id = models.ForeignKey(CustomUser,verbose_name='ユーザID', max_length=15, on_delete=models.PROTECT)
    schedule_do = models.TextField(verbose_name='やるべきこと', max_length=40)
    schedule_priority = models.IntegerField(verbose_name='優先度', max_length=1, default=2)
    schedule_start_date = models.DateTimeField(verbose_name='開始日時', auto_now=True)
    schedule_end_date = models.DateTimeField(verbose_name='終了日時', auto_now=True)
    schedule_start_hour = models.DateTimeField(verbose_name='開始日時(時)', default=0)
    schedule_start_min = models.DateTimeField(verbose_name='開始日時(分)', default=0)
    schedule_end_hour = models.DateTimeField(verbose_name='終了日時(時)', default=0)
    schedule_end_min = models.DateTimeField(verbose_name='終了日時(分)', default=0)
    schedule_worktime = models.IntegerField(verbose_name='一日の作業時間', max_length=3)
    sucedule_creation_stage = models.IntegerField(verbose_name='作成段階', max_length=3)

    class Meta:
        verbose_name_plural = 'rakusuke_schedule'

    def __str__(self):
        return self.title
