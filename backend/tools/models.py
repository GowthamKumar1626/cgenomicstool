from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


class ToolsModel(models.Model):
    """
    ToolsModel is a class which gives the information about each tool that will be
    implemented in this web interface.
    
    Crosstab: Crosstab helps to find gene presence or absence among genomes of input. Will be able to give a pictorial understanding of the pattern of genes composed in various genomes through plots.
    """
    class Meta:
        verbose_name_plural = "ToolsModel"
    
    # _id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(primary_key=True, editable=True, max_length=200, unique=True)
    href = models.CharField(max_length=100, unique=True, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey('auth.User', related_name='tools', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ('created_at', )
      
    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        super(ToolsModel, self).save(*args, **kwargs)
    
    
    