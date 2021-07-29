from django.db.models.signals import pre_save
from django.contrib.auth.models import User

def updateUser(sender, instance, **kwargs):
    user = instance
    if user.email != '':
        user.username = user.email
    print('Signal Triggered!')
    
pre_save.connect(updateUser, sender=User)