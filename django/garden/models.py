from django.db import models
from django.utils import timezone


class Vegetable(models.Model):
    """野菜"""
    name = models.CharField('名前', max_length=100)
    price = models.IntegerField('値段', default=0)
    description = models.TextField('説明')
    producer = models.CharField('生産者', max_length=50, default='ウメ')
    sold_out = models.BooleanField(
        '売り切れ', help_text="売り切れの場合True", default=False)
    created_at = models.DateTimeField(default=timezone.now)
