from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
'''def january(request):
    return HttpResponse('for january')


def february(request):
    return HttpResponse('for february')

def march(request):
    return HttpResponse('for march')'''


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'This is January!'
    elif month == 'february':
        challenge_text = 'This is February!'
    elif month == 'march':
        challenge_text = 'This is march!'
    else:
        return HttpResponseNotFound('Too far ahead we are not there yet.!')
    return HttpResponse(challenge_text)


