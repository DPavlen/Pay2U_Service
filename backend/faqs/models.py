from django.db import models
from users.models import MyUser


class Faq(models.Model):
    """
    Класс для хранения списка часто задаваемых вопросов.

    question - часто задаваемый вопрос
    answer - ответ на заданный вопрос
    created - дата создания вопроса
    updated - дата обновленя вопроса
    author - пользователь, создавший вопрос/ответ.
    """

    objects = None
    question = models.CharField(max_length=250, verbose_name="Вопрос")
    answer = models.CharField(max_length=1000, verbose_name="Ответ")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        MyUser, on_delete=models.PROTECT, verbose_name="Создатель вопроса"
    )

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQS"
        ordering = ["-created"]
        indexes = [
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return self.question
