from django.db import models


class BaseModel(models.Model):
    is_del = models.BooleanField(default=False, verbose_name='是否删除')
    crt_ts = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    upd_ts = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        abstract = True
