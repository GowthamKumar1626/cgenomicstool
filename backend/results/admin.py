from django.contrib import admin

from .models import ResultModel

@admin.register(ResultModel)
class ResultModelAdmin(admin.ModelAdmin):
    list_display = ["job_id", "is_user", "user_id", "tool_used", "created_at", "expires_at"]
