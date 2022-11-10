from django.db import models
from accounts.models import CustomUser

class RakusukeSchedule(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    schedule_do = models.TextField(verbose_name='やるべきこと', max_length=40)
    # やるべきことをスケジュールに修正
    schedule_priority = models.IntegerField(verbose_name='優先度', default=2)
    schedule_start_date = models.DateTimeField(verbose_name='開始日時', auto_now=True)
    schedule_end_date = models.DateTimeField(verbose_name='終了日時', auto_now=True)
    schedule_worktime = models.IntegerField(verbose_name='１日の作業時間')
    schedule_creation_stage = models.IntegerField(verbose_name='作成段階')
    schedule_ditching = models.TextField(verbose_name='サボり日', blank=True, null=True)
    schedule_category = models.IntegerField(verbose_name='カテゴリ')

    class Meta:
        verbose_name_plural = 'RakusukeSchedule'

    def __str__(self):
        return self.title
