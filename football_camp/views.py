from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello football players')

def home(request):
    return render(request, 'football_camp/base.html')
