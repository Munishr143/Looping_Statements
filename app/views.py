from django.shortcuts import render

# Create your views here.


def Loop(request):
    d={'name':'MUNISH_R'}
    return render(request, 'loop.html', context=d)
