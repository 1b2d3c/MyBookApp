from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    '''AbstractUserの全フィールドを継承
    '''
    birthday = models.DateField(null=True)


