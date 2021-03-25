from django.db import models
from django.core.files.images import ImageFile
from django.core.files.uploadedfile import UploadedFile
from django.db.models.signals import post_save, pre_delete

from .handlers import upload_location, genereate_id

# Model for Saving IPAddress and corresponding JobID
class IPAddressModel(models.Model):
    job_id = models.CharField(
        max_length=200, 
        default=genereate_id, 
        blank=False, 
        primary_key=True
    )
    ip_address = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return self.job_id

# Results like image and csv file is saved under this model
class ResultModel(models.Model):
    
    job_id = models.ForeignKey(IPAddressModel, auto_created=True, on_delete=models.CASCADE)
    image = models.ImageField()
    data = models.FileField(upload_to=upload_location)

# Signals (Similar to Trigger) - When ever a JobID is created under a particular IP its corrsponding results are automatically saved under this model
def create_resultmodel_record(sender, instance, created, **kwargs):
    if created:
        # ResultModel.objects.create(job_id = instance, image="./outputs/crosstab.png")
        record = ResultModel.objects.create(job_id=instance)
        record.image = ImageFile(open("./cgenomicstool/static/img/crosstab.png", "rb"))
        record.data = UploadedFile(open("./cgenomicstool/static/files/crosstab.csv", "rb"))
        record.save()

# After save command applied on IPAddressModel a signal is created to CRUD operation on ResultModel
post_save.connect(create_resultmodel_record, sender = IPAddressModel)

