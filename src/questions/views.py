from django.shortcuts import render, Http404

# Create your views here.

from .forms import UserResponseForm
from .models import Question, Answer

def single(request, id):
    if request.user.is_authenticated():
        form = UserResponseForm(request.POST or None)
        if form.is_valid():
            question_id = form.cleaned_data.get('question_id')
            answer_id = form.cleaned_data.get('answer_id')
            question_instance = Question.objects.get(id=answer_id)
            answer_instance = Answer.objects.get(id=answer_id)
            print answer_instance.text, question_instance.text

        queryset = Question.objects.all().order_by('-timestamp')
        instance = queryset[0]
        context = {
            "form": form,
            "instance": instance,
        }
        return render(request, "questions/home.html", context)
    else:
        raise Http404



def home(request):
    if request.user.is_authenticated():
        form = UserResponseForm(request.POST or None)
        if form.is_valid():
            question_id = form.cleaned_data.get('question_id')
            answer_id = form.cleaned_data.get('answer_id')
            question_instance = Question.objects.get(id=answer_id)
            answer_instance = Answer.objects.get(id=answer_id)
            print answer_instance.text, question_instance.text

        queryset = Question.objects.all().order_by('-timestamp')
        instance = queryset[0]
        context = {
            "form": form,
            "instance": instance,
        }
        return render(request, "questions/home.html", context)
    else:
        raise Http404
