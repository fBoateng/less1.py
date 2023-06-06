from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    'january': 'This is January!',
    'february': 'This is February',
    'march': 'This is March!',
    'april': 'This is April',
    'may': 'This is May!',
    'june': 'This is June',
    'july': 'This is July!',
    'august': 'This is August',
    'september': 'This is September!',
    'october': 'This is October',
    'november': 'This is November!',
    'december': 'This is December',   
}


# Create your views here.
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound('There are 12 months please enter 1.')
    
    forward_month = months[month-1]
    redirect_path = reverse('month-challenges', args=[forward_month])
    return HttpResponseRedirect('/challenges/' + forward_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f'<h1>{challenge_text}</h1>'
    except:
        return HttpResponseNotFound('<h1>Month not found!</h1>')
    return HttpResponse(response_data)


