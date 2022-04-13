from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from utilisateur import settings


class CustomUser(AbstractUser):
   pass
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    
def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)
