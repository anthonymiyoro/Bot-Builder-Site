from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from .forms import UserResponseForm
from .models import Question, Answer


def single(request, id):
    # checks to see if the question exists and if it doesnt gives a 404
    if request.user.is_authenticated():
        form = UserResponseForm(request.POST or None)
        if form.is_valid():
            question_id = form.cleaned_data.get('question_id')
            answer_id = form.cleaned_data.get('answer_id')
            question_instance = Question.objects.get(id=answer_id)
            answer_instance = Answer.objects.get(id=answer_id)
            print answer_instance.text, question_instance.text
            next_q = Question.objects.all().order_by("?").first()
            return redirect("question_single", id=next_q.id)

        queryset = Question.objects.all().order_by('-timestamp')
        instance = get_object_or_404(Question, id=id)
        context = {
            "form": form,
            "instance": instance,
        }
        return render(request, "questions/single.html", context)
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
