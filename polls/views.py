from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World. You are at the polls index.')

def detail(request,question_id):
    return HttpResponse(f'You are looking at question {question_id}')

def results(request, question_id):
    response = f'You are looking at the results of the question {question_id}'
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f'You are voting on question {question_id}')