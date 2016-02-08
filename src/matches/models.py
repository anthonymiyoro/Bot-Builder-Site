from django.conf import settings
from django.db import models


# Create your models here.

class MatchManager(models.Manager):
    def get_or_create_match(self,  user_a=None, user_b=None):
        try:
            obj = self.get(user_a=user_a, user_b=user_b)
        except:
            obj = None
        try:
            obj_2 = self.get(user_a=user_b, userb=user_a)
        except:
            obj_2 = None
        if obj and not obj_2:
            return obj, False
        elif not obj and obj_2:
            return obj_2, False
        else:
            new_instance = self.create(user_a=user_a, user_b=user_b)
            new_instance.match_decimal = 0.85
            new_instance.questions_answered = 20
            new_instance.save()
            return new_instance, True


class Match(models.Model):
    user_a = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='match_user_a')
    user_b = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='match_user_b')
    match_decimal = models.DecimalField(decimal_places=8, max_digits=16, default=0.00)
    questions_answered = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.match_decimal = 0.85

