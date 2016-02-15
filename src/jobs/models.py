from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify

# Create your models here.
User = settings.AUTH_USER_MODEL


class Location(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField()
    active = models.BooleanField(default=True)
    flagged = models.ManyToManyField(User, blank=True)

    def __unicode__(self):  # __str__(self):
        return self.name


def pre_save_location(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)


pre_save.connect(pre_save_location, sender=Location)
