from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    '''
    User profile
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=80, default='My Bio', blank=True)

    def __str__(self):
        return self.bio