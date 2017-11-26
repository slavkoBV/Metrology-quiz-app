from django.contrib import admin

from .models import QuestionCategory, Question, Answer, Quiz


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'description']
    inlines = [AnswerInline, ]
    ordering = ('id',)


class QuizAdmin(admin.ModelAdmin):
    filter_horizontal = ('questions',)
    ordering = ('id',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionCategory)
admin.site.register(Quiz, QuizAdmin)
