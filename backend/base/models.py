import datetime
from django.db import models
from django.contrib.auth.models import User

from tools.models import ToolsModel


def user_directory_path(instance, filename):
# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.username, filename)

def result_id_generator():
# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f"result-id-{datetime.datetime.now()}"

class Result(models.Model):
    class Meta:
        verbose_name_plural = 'ResultModel'
        ordering = ('result_id', )
        
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    result_id = models.CharField(unique=True, max_length = 200, editable=True, default=result_id_generator)

    def __str__(self):
        return str(self.result_id)

class ResultItem(models.Model):
    class Meta:
        verbose_name_plural = 'ResultItemModel'
        ordering = ('result_id', )
        
    result = models.ForeignKey(Result, on_delete=models.SET_NULL, null=True)
    tool = models.ForeignKey(ToolsModel, on_delete=models.SET_NULL, null=True)
    results = models.FileField(null=True, upload_to="files")
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

