from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Service(models.Model):
    TRAININGS = (("skills", "Skills"), ("fitness", "Fitness"), ("tactics", "Tactics"))
    focus = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    features = models.TextField()
    training = models.CharField(max_length=10, choices=TRAININGS, null=True, blank=True)

    def __str__(self):
        return self.focus

class Player(models.Model):
    GENDERS = (("male", "Male"), ("female", "Female"))
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=10, validators=[MinValueValidator(10), MaxValueValidator(14)])
    gender = models.CharField(max_length=6, choices=GENDERS)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.focus} - {self.player.name}"
