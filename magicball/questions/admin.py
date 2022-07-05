from django.contrib import admin
from .models import Answers, History

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    pass

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    pass