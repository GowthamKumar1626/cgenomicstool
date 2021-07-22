from django.contrib import admin

from .models import ToolsModel, CrosstabResults

# Register your models here.

admin.site.register(ToolsModel)
admin.site.register(CrosstabResults)
# admin.site.register(NonUserModel)