from django.db import models
from django.contrib.auth.models import User


class Answers(models.Model):
    answer = models.CharField(max_length=150, verbose_name='Ответ')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class History(models.Model): #таблица для хронологии
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id пользователя')
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE, verbose_name='id ответа')
    question = models.TextField(verbose_name='Вопрос')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'История'
        ordering = ['created_date']