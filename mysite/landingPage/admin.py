from django.contrib import admin
from .models import UserActionHistory


@admin.register(UserActionHistory)
class UserActionHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'action', 'choice', 'timestamp')
    list_filter = ('action', 'timestamp','choice')
    search_fields = ('user__username', 'question__question_text', 'choice__choice_text')
    
    def choice_text(self, obj):
        return obj.choice.choice_text if obj.choice else 'None'
    
    choice_text.short_description = 'Choice'