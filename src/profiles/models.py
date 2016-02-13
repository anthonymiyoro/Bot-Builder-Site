from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL

def upload_location(instance, filename):

    location = str(instance.user.username)
    return "%s/%s" %(location)

class Profile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=120, null=True, blank=True)
    picture = models.ImageField(upload_to=upload_location, null=True, blank=True)