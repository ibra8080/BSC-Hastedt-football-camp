from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Service, Player, Booking
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    return HttpResponse('Hello football players')

def home(request):
    return render(request, 'football_camp/base.html')


def admin_create_service(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        focus = request.POST.get('focus')
        duration = request.POST.get('duration')
        features = request.POST.get('features')
        training = request.POST.get('training')
        
        Service.objects.create(
            title=title,
            focus=focus,
            duration=duration,
            features=features,
            training=training
        )
        
        return redirect('admin_manage_services')

    return render(request, 'football_camp/admin_create_service.html')

def admin_manage_services(request):
    services = Service.objects.all()
    return render(request, 'football_camp/admin_manage_services.html', {'services': services})


def book_service(request):
    if request.method == 'POST':
        user = request.user
        player_id = request.POST.get('player_id')
        service_ids = request.POST.getlist('service_ids')  # Adjust the form parameter accordingly

        player = get_object_or_404(Player, id=player_id)
        booking = Booking.objects.create(user=user, player=player)

        for service_id in service_ids:
            service = get_object_or_404(Service, id=service_id)
            booking.services.add(service)

        booking.save()
        return redirect('player_profile', player_id=player_id)

    players = Player.objects.all()
    services = Service.objects.all()
    return render(request, 'football_camp/book_service.html', {'players': players, 'services': services})


def player_profile(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    bookings = Booking.objects.filter(player=player)
    return render(request, 'football_camp/player_profile.html', {'player': player, 'bookings': bookings})


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


def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        service.title = request.POST.get('title')
        service.focus = request.POST.get('focus')
        service.duration = request.POST.get('duration')
        service.features = request.POST.get('features')
        service.training = request.POST.get('training')
        service.save()
        return redirect('admin_manage_services')

    return render(request, 'football_camp/edit_service.html', {'service': service})


def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    return redirect('admin_manage_services')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})