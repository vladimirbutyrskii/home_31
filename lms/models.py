from django.db import models

NULLABLE = dict(null=True, blank=True)


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )
    preview = models.ImageField(
        upload_to="lms/preview",
        **NULLABLE,
        verbose_name="Эмблема курса",
        help_text="Загрузите эмблему курса",
    )
    description = models.TextField(
        **NULLABLE,
        verbose_name="Описание курса",
        help_text="Укажите описание курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ("pk",)


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Укажите название урока",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        help_text="Выберите курс",
        related_name="lessons",
    )
    description = models.TextField(
        **NULLABLE,
        verbose_name="Описание урока",
        help_text="Укажите описание урока",
    )
    preview = models.ImageField(
        upload_to="lms/preview",
        **NULLABLE,
        verbose_name="Эмблема урока",
        help_text="Загрузите эмблему урока",
    )
    link_video = models.URLField(
        max_length=150,
        **NULLABLE,
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ("pk",)
