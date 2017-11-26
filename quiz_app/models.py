from django.db import models


class QuestionCategory(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Категорія питань'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Опис категорії'
    )

    class Meta:
        verbose_name = 'Категорія питань'
        verbose_name_plural = 'Категорії питань'

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(
        max_length=50,
        help_text='Вкажіть коротко (не більше 50-ти символів) зміст питання',
        null=True,
        blank=True,
        verbose_name='Короткий зміст'
    )
    description = models.TextField(
        verbose_name='Зміст питання'
    )
    category = models.ForeignKey(
        QuestionCategory,
        verbose_name='Категорія'
    )


    class Meta:
        verbose_name = 'Питання'
        verbose_name_plural = 'Питання'

    def __str__(self):
        return str(self.id) + ' ' + self.title


class Answer(models.Model):
    description = models.TextField(
        verbose_name='Зміст відповіді'
    )
    question = models.ForeignKey(
        Question,
        related_name='question',
        verbose_name='Номер питання')
    true_answer = models.BooleanField(
        verbose_name='Правильна відповідь',
        default=False
    )

    class Meta:
        verbose_name = 'Відповідь'
        verbose_name_plural = 'Відповіді'

    def __str__(self):
        return str(self.id)


class Quiz(models.Model):
    questions = models.ManyToManyField(
        Question,
        blank=True,
        related_name='tests',
        verbose_name='Питання до тесту'
    )

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тести'

    def __str__(self):
        return 'Варіант № ' + str(self.id)
