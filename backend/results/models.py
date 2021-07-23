from tools.models import ToolsModel
from django.db import models

import datetime

def user_directory_path(instance, filename):
# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.username, filename)

def result_id_generator():
# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f"result-id-{datetime.datetime.now()}"
    
class ResultsModel(models.Model):
    class Meta:
        verbose_name_plural = 'ResultsModel'
        ordering = ('result_id', )
    
    result_id = models.CharField(primary_key=True, max_length = 200, editable=True, default=result_id_generator)
    upload_results = models.FileField(upload_to="files", null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    tool_used = models.ForeignKey(ToolsModel, related_name='tools', null=True, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='results', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.result_id
    
    def save(self, *args, **kwargs):
        super(ResultsModel, self).save(*args, **kwargs)


