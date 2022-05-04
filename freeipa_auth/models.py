from django.contrib.auth.models import AbstractUser
from django.db import models


class ScUser(AbstractUser):
    full_name = models.CharField(verbose_name='ФИО', max_length=128, blank=True)
    post = models.CharField(verbose_name='должность', max_length=128, blank=True)
    department = models.CharField(verbose_name='Отдел', max_length=256, blank=True)
    updated = models.DateTimeField(verbose_name='Дата последнего входа', auto_now=True)

