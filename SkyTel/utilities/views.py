import os
from django.shortcuts import render


def ping(request):
    context = {}
    if request.GET.get('q', False) == '':
        context['ping_output'] = 'Please enter ip address!'

    elif 'q' in request.GET:
        ping_output = os.popen('ping -n 10 ' + request.GET['q']).read()
        context['ping_output'] = ping_output

    return render(request, 'utilities/ping.html', context)


def traceroute(request):
    context = {}
    if request.GET.get('q', False) == '':
        context['ping_output'] = 'Please enter ip address!'

    elif 'q' in request.GET:
        ping_output = os.popen('tracert ' + request.GET['q']).read()
        context['ping_output'] = ping_output

    return render(request, 'utilities/traceroute.html', context)