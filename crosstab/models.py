from django.db import models
from django.core.files.images import ImageFile
from django.db.models.signals import post_save, pre_delete

from .handlers import upload_location, genereate_id

from datetime import datetime
import base64


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


class ResultModel(models.Model):
    
    job_id = models.ForeignKey(IPAddressModel, auto_created=True, on_delete=models.CASCADE)
    image = models.ImageField()
    # data = models.FileField(null=True, upload_to=upload_location)

    # def __str__(self):
    #     return self.job_id


def create_resultmodel_record(sender, instance, created, **kwargs):
    if created:
        # ResultModel.objects.create(job_id = instance, image="./outputs/crosstab.png")
        r = ResultModel.objects.create(job_id=instance)
        r.image = ImageFile(open("./cgenomicstool/static/img/crosstab.png", "rb"))
        r.save()

post_save.connect(create_resultmodel_record, sender = IPAddressModel)

