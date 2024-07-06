from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Service, Player, Booking
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return HttpResponse('Hello football players')

def home(request):
    return render(request, 'football_camp/base.html')

def service_list(request):
    services = Service.objects.all()
    return render(request, 'football_camp/service_list.html', {'services': services})

def book_service(request):
    if request.method == 'POST':
        user = request.user
        player_id = request.POST.get('player_id')
        service_id = request.POST.get('service_id')

        player = Player.objects.get(id=player_id)
        service = Service.objects.get(id=service_id)

        Booking.objects.create(user=user, player=player, service=service)

        return redirect('service_list')

    players = Player.objects.all()
    services = Service.objects.all()
    return render(request, 'football_camp/book_service.html', {'players': players, 'services': services})