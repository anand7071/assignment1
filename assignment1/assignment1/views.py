from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def savefile(request):
    print(request.GET.get('text','default'))
    return HttpResponse("you are now logged in ")