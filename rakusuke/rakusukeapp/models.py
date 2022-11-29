from django.db import models
from accounts.models import CustomUser

import datetime
from django import forms


class RakusukeSchedule(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    schedule_do = models.TextField(verbose_name='スケジュール', max_length=40)
    schedule_date = models.DateField(verbose_name='日付')
    schedule_priority = models.IntegerField(verbose_name='優先度', default=2)
    schedule_start_date = models.DateField(verbose_name='開始日時', auto_now=True)
    schedule_end_date = models.DateField(verbose_name='終了日時', auto_now=True)
    schedule_worktime = models.IntegerField(verbose_name='１日の作業時間')
    schedule_creation_stage = models.IntegerField(verbose_name='作成段階')
    schedule_ditching = models.TextField(verbose_name='サボり日', blank=True, null=True)
    schedule_category = models.IntegerField(verbose_name='カテゴリ', default=2)
    schedule_achieved = models.IntegerField(verbose_name='スケジュール達成済み')
    schedule_subject = models.TextField(verbose_name='科目')

    class Meta:
        verbose_name_plural = 'スケジュールテーブル'

    def __str__(self):
        return self.title


class RakusukeFunny(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    funny_onoff = models.IntegerField(verbose_name='面白機能ONOFF')

    class Meta:
        verbose_name_plural = '面白機能テーブル'

    def __str__(self):
        return self.title


class RakusukeSubject(models.Model):
    subject_name = models.TextField(verbose_name='科目名')
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = '科目テーブル'

    def __str__(self):
        return self.title


class RakusukeDetail(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    subject_id = models.ForeignKey(RakusukeSubject, verbose_name='科目ID', on_delete=models.PROTECT)
    detail_name = models.TextField(verbose_name='詳細名')
    detail_achieved = models.IntegerField(verbose_name='タスク達成済み')

    class Meta:
        verbose_name_plural = '詳細テーブル'

    def __str__(self):
        return self.title


class RakusukeFixed(models.Model):
    ADAPTATIONS = (
        (1, "月"),
        (2, "火"),
        (3, "水"),
        (4, "木"),
        (5, "金"),
        (6, "土"),
        (7, "日"),
    )

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    fixed_do = models.TextField(verbose_name='固定スケジュール')
    fixed_start_time = models.TimeField(verbose_name='開始時間')
    fixed_end_time = models.TimeField(verbose_name='終了時間')
    fixed_adaptation = models.IntegerField(verbose_name='適応日', choices=ADAPTATIONS, default=1)

    class Meta:
        verbose_name_plural = '固定スケジュールテーブル'

    def __str__(self):
        return self.title
