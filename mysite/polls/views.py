from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

def get_question_or_404(question_id):
    return get_object_or_404(Question, pk=question_id)

def detail_or_results(request, question_id, template_name):
    question = get_question_or_404(question_id)
    return render(request, template_name, {"question": question})

@login_required
def detail(request, question_id):
    return detail_or_results(request, question_id, "polls/detail.html")

@login_required
def results(request, question_id):
    return detail_or_results(request, question_id, "polls/results.html")

@login_required
def vote(request, question_id):
    question = get_question_or_404(question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))

#display
@login_required
def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
