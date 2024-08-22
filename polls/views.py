from django.http import HttpResponse
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request,question_id):
    return HttpResponse(f'You are looking at question {question_id}')

def results(request, question_id):
    response = f'You are looking at the results of the question {question_id}'
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f'You are voting on question {question_id}')