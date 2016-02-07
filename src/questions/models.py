from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save


# Create your models here.

class Question(models.Model):
    text = models.TextField()
    active = models.BooleanField(default=True)
    draft = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.text[:10]


class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField(max_length=120)
    active = models.BooleanField(default=True)
    draft = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.text[:10]


LEVELS = (
    ('Mandatory', 'Mandatory'),
    ('Very Important', 'Very Important'),
    ('Somewhat Important', 'Somewhat Important'),
    ('Not Important', 'Not Important'),
)


class UserAnswer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    question = models.ForeignKey(Question)
    my_answer = models.ForeignKey(Answer, related_name='user_answer')
    my_answer_importance = models.CharField(max_length=55, choices=LEVELS)
    my_points = models.IntegerField(default=-1)
    # the answer field is allowed to be blank
    their_answer = models.ForeignKey(Answer, null=True, blank=True)
    their_importance = models.CharField(max_length=55, choices=LEVELS)
    their_points = models.IntegerField(default=-1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.my_answer.text[:10]


# list of scores per importance
def score_importance(importance_level):
    if importance_level == "Mandatory":
        points = 300
    elif importance_level == "Very Important":
        points = 200
    elif importance_level == "Somewhat Important":
        points = 50
    elif importance_level == "Not Important":
        points = 0
    else:
        points = 0



def update_user_answer_score(sender, instance,  *args, **kwargs):
    my_points = score_importance(instance.my_answer_importance)
    instance.my_points = my_points
    their_points = score_importance(instance.their_importance)
    instance.their_points = their_points


pre_save.connect(update_user_answer_score, sender=UserAnswer)




# def update_user_answer_score(sender, instance, created, *args, **kwargs):
#     print sender
#     print instance
#     print created
#     if created:
#         if instance.my_points == -1:
#             my_points = score_importance(instance.my_answer_importance)
#             instance.my_points = my_points
#             instance.save()
#
#         if instance.my_points == -1:
#             their_points = score_importance(instance.their_importance)
#             instance.their_points = their_points
#             instance.save()
#
# post_save.connect(update_user_answer_score, sender=UserAnswer)
#

