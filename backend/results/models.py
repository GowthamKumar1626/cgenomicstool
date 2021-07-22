from datetime import datetime, timedelta

import django
from backend import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import activate

from . import handlers

# Create your models here.

activate(settings.TIME_ZONE)

def dataset_directory_path(instance, filename):
    return 'user_{0}/crosstab_dataset/{1}'.format(instance.user_id, filename)

class ResultModel(models.Model):
    class Meta:
        verbose_name_plural = "ResultsModel"
    
    job_id = models.CharField(
        max_length=200, 
        default=handlers.genereate_id, 
        blank=False, 
        primary_key=True
    )
    is_user = models.BooleanField(null=True, blank=True, default=True)
    user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    TOOLS_PRESENT_IN_DB = [
        ('Crosstab', 'Crosstab'),
        ('Gene Organisation', 'Gene Organisation'),
    ]
    tool_used = models.CharField(
        max_length=20,
        choices=TOOLS_PRESENT_IN_DB,
        default='Tool removed from DB',
        null = False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=datetime.today() + timedelta(days=30))

    result_data = models.FileField(upload_to=dataset_directory_path, null=True, blank=True)

    def __str__(self) -> str:
        return self.job_id







    