from django.db import models

class ToolsModel(models.Model):
    class Meta:
        verbose_name_plural = 'ToolModel'
        ordering = ('name', )
        
    name = models.CharField(primary_key=True, editable=True, unique=True, max_length=100)
    image = models.FileField(upload_to='images')
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(ToolsModel, self).save(*args, **kwargs)    
    