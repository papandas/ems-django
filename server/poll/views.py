from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Question, Answer, Choice
# Create your views here.

def index(request):
    questions = Question.objects.all()
    print("Questions ", questions)
    context = {}
    context['title'] = 'All Polls'
    context['questions'] = questions
    return render(request, 'poll/index.html', context)

def details(request, id=None):
    question = get_object_or_404(Question, pk=id)
    context = {}
    context['title'] = 'Poll Detail'
    context['question'] = question
    #context['choices'] = ''
    return render(request, 'poll/detail.html', context)

def vote(request, id=None):

    if request.method == "GET":
        question = get_object_or_404(Question, pk=id)
        context = {}
        context['title'] = 'Vote'
        context['question'] = question
        return render(request, 'poll/vote.html', context)
    else:
        #user = User.objects.get(id=1)
        data = request.POST

        ret = Answer.objects.create(user_id=1, choice_id=data['choice'] )
        if ret:
            return HttpResponse('Your vote is succefully created')
        else:
            return HttpResponse('Your vote has missed.')
        #return render(request, 'poll/detail.html', context)