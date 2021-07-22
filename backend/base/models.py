from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToolsModel(models.Model):
    class Meta:
        verbose_name = "ToolsModel"

    _id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    href = models.CharField(max_length=100, unique=True, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return self.name

def dataset_directory_path(instance, filename):
    return 'user_{0}/crosstab_dataset/{1}'.format(instance.user, filename)


class CrosstabResults(models.Model):
    class Meta:
        verbose_name_plural = "CrosstabResults"
    
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    crosstab_dataset = models.FileField(upload_to=dataset_directory_path, null=True, blank=True)


    
    