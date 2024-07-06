from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Service, Player, Booking
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return HttpResponse('Hello football players')

def home(request):
    return render(request, 'football_camp/base.html')


def admin_create_service(request):
    if request.method == 'POST':
        service_name = request.POST.get('service_name')
        Service.objects.create(name=service_name)
        return redirect('admin_manage_services')

    return render(request, 'football_camp/admin_create_service.html')

def admin_manage_services(request):
    services = Service.objects.all()
    return render(request, 'football_camp/admin_manage_services.html', {'services': services})


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


def view_training_schedule(request):
    # Assuming you have a TrainingSchedule model
    schedule = TrainingSchedule.objects.all()
    return render(request, 'football_camp/view_training_schedule.html', {'schedule': schedule})


def manage_players(request):
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        Player.objects.create(name=player_name)
        return redirect('manage_players')

    players = Player.objects.all()
    return render(request, 'football_camp/manage_players.html', {'players': players})


def service_list(request):
    services = Service.objects.all()
    return render(request, 'football_camp/service_list.html', {'services': services})
