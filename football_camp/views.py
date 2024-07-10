from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Service, Player, Booking
from .forms import CustomUserCreationForm, PlayerForm

# Create your views here.
def index(request):
    return HttpResponse('Hello football players')

def home(request):
    services = Service.objects.all()
    return render(request, 'football_camp/home.html', {'services': services})

def is_superuser(user):
    return user.is_superuser

# Admin Functions

def superuser_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, "You don’t have permission to access this page.")
            return redirect('service_list')
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func

@superuser_required
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

@superuser_required
def admin_manage_services(request):
    services = Service.objects.all()
    return render(request, 'football_camp/admin_manage_services.html', {'services': services})

@superuser_required
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

@superuser_required
def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    return redirect('admin_manage_services')


# User Functions 

@login_required
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


@login_required
def player_profile(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    bookings = Booking.objects.filter(player=player)
    return render(request, 'football_camp/player_profile.html', {'player': player, 'bookings': bookings})


@login_required
def view_training_schedule(request):
    # Assuming you have a TrainingSchedule model
    schedule = TrainingSchedule.objects.all()
    return render(request, 'football_camp/view_training_schedule.html', {'schedule': schedule})


@login_required
def manage_players(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_players')
    else:
        form = PlayerForm()

    players = Player.objects.all()
    return render(request, 'football_camp/manage_players.html', {'players': players, 'form': form})


def service_list(request):
    services = Service.objects.all()
    return render(request, 'football_camp/service_list.html', {'services': services})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})