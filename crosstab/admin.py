from django.contrib import admin
from .models import ResultModel, IPAddressModel

@admin.register(IPAddressModel)
class IPAddressAdmin(admin.ModelAdmin):
    list_display = ["job_id", "ip_address", "title", "created_on", "expires_on"]

@admin.register(ResultModel)
class ResultAdmin(admin.ModelAdmin):
    # list_display = ["job_id", "image", "data"]
    list_display = ["job_id", "image", "data", "encodings"]
