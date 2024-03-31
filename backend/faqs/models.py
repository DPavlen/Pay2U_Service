from django.db import models


class Faq(models.Model):
    """
    Класс для хранения списка часто задаваемых вопросов.

    topic_question - тема вопроса
    question - часто задаваемый вопрос
    answer - ответ на заданный вопрос
    created - дата создания вопроса
    updated - дата обновленя вопроса
    сategory - категория к кторой относится вопрос.
    """

    class Category(models.TextChoices):
        REGISTRATION = "registration", "Оформление"
        CONNECTION = "connection", "Подключение"
        WORK_WITH_SUBSCRIPTIONS = "work_with_subscriptions", "Работа с подписками"

    topic_question = models.CharField(
        max_length=250,
        verbose_name="Тема вопроса"
    )
    сategory = models.CharField(
        max_length=25,
        choices=Category.choices,
        verbose_name="категория вопроса",
    )
    question = models.CharField(
        max_length=250,
        verbose_name="Вопрос"
    )
    answer = models.CharField(
        max_length=1000,
        verbose_name="Ответ"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания вопроса"
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления вопроса"
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
