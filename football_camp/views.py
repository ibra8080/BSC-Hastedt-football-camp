from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Service, Player, Booking
from .forms import CustomUserCreationForm, PlayerForm
from django.contrib.auth import authenticate, login, logout


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
    user = request.user
    players = Player.objects.filter(user=user)
    
    if not players.exists():
        messages.info(request, "You need to add a player first. Please add a player.")
        return redirect('manage_players')

    if request.method == 'POST':
        player_id = request.POST.get('player_id')
        service_ids = request.POST.getlist('service_ids')

        player = get_object_or_404(Player, id=player_id)
        booking = Booking.objects.create(user=user, player=player)

        for service_id in service_ids:
            service = get_object_or_404(Service, id=service_id)
            booking.services.add(service)

        booking.save()
        return redirect('player_profile', player_id=player_id)

    services = Service.objects.all()
    return render(request, 'football_camp/book_service.html', {'players': players, 'services': services})


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.user != request.user:
        messages.error(request, "You do not have permission to edit this booking.")
        return redirect('home')
    if request.method == 'POST':
        player_id = request.POST.get('player_id')
        service_ids = request.POST.getlist('service_ids')
        
        booking.player = get_object_or_404(Player, id=player_id)
        booking.services.clear()
        
        for service_id in service_ids:
            service = get_object_or_404(Service, id=service_id)
            booking.services.add(service)
        
        booking.save()
        return redirect('player_profile', player_id=booking.player.id)
    
    players = Player.objects.filter(user=request.user)
    services = Service.objects.all()
    return render(request, 'football_camp/edit_booking.html', {'booking': booking, 'players': players, 'services': services})

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.user != request.user:
        messages.error(request, "You do not have permission to delete this booking.")
        return redirect('home')
    if request.method == 'POST':
        player_id = booking.player.id
        booking.delete()
        return redirect('player_profile', player_id=player_id)
    return render(request, 'football_camp/confirm_delete_booking.html', {'booking': booking})


@login_required
def player_profile(request, player_id):
    player = get_object_or_404(Player.objects.select_related('user'), id=player_id)
    if player.user != request.user:
        messages.error(request, "You do not have permission to view this player's profile.")
        return redirect('home')
    bookings = Booking.objects.filter(player=player).select_related('user').prefetch_related('services')
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
            player = form.save(commit=False)
            player.user = request.user
            player.save()
            messages.success(request, "Your player was successfully added.")
            return render(request, 'football_camp/manage_players.html', {
                'form': PlayerForm(),
                'players': Player.objects.filter(user=request.user),
                'success': True
            })
    else:
        form = PlayerForm()

    players = Player.objects.filter(user=request.user)
    return render(request, 'football_camp/manage_players.html', {'players': players, 'form': form})

@login_required
def player_added(request):
    return render(request, 'football_camp/player_added.html')


@login_required
def user_account(request):
    user = request.user
    players = Player.objects.filter(user=user)
    context = {
        'user': user,
        'players': players,
    }
    return render(request, 'football_camp/user_account.html', context)


def service_list(request):
    services = Service.objects.all()
    return render(request, 'football_camp/service_list.html', {'services': services})


def service_page(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'football_camp/service_page.html', {'service': service})
    

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect('login')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/')  

@login_required
def edit_player(request, player_id):
    player = get_object_or_404(Player, id=player_id, user=request.user)
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            messages.success(request, 'Player updated successfully.')
            return redirect('user_account')
    else:
        form = PlayerForm(instance=player)
    return render(request, 'football_camp/edit_player.html', {'form': form, 'player': player})


@login_required
def delete_player(request, player_id):
    player = get_object_or_404(Player, id=player_id, user=request.user)
    if request.method == 'POST':
        player.delete()
        messages.success(request, 'Player deleted successfully.')
        return redirect('user_account')
    return render(request, 'football_camp/confirm_delete_player.html', {'player': player})