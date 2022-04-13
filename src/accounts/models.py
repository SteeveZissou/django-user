from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    '''
    custom user class
    '''
    zip_code = models.CharField(blank=True, max_length=5)


