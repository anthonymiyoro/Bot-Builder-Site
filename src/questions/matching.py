from django.contrib.auth import get_user_model

from questions.models import UserAnswer

User = get_user_model()

users = User.objects.all
all_user_answers = UserAnswer.objects.all().order_by("user__id")


def get_match(user_a, user_b):
    user_a_answers = UserAnswer.objects.filter(user=user_a)[0]
    user_b_answers = UserAnswer.objects.filter(user=user_b)[0]

    if user_a_answers.question.id == user_b_answers.question.id:
        user_a_answer = user_a_answers.my_answer
        user_a_pref = user_a_answers.their_answer
        user_b_answer = user_b_answers.my_answer
        user_b_pref = user_b_answers.their_answer

        if user_a_answer == user_b_pref:
            print "user a fits with user b's preference"

        if user_a_pref == user_b_answer:
        print "user b fits with user a's preference"

        if user_a_answer == user_b_pref && user_a_pref == user_b_answer
            print "this is an ideal answer for both"