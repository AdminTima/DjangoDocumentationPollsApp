from django.contrib import admin
from . import models


class ChoiceInLine(admin.TabularInline):
    model = models.Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]
    list_display = ['question_text', 'pub_date', 'was_published_recently']


admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice)
