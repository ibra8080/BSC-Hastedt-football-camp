from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Service(models.Model):
    TRAININGS = (("skills", "Skills"), ("fitness", "Fitness"), ("tactics", "Tactics"), ("all", "All"))
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Service Title")
    focus = models.CharField(max_length=200, verbose_name="Service Focus")
    duration = models.CharField(max_length=100, verbose_name="Service Duration")
    features = models.TextField(verbose_name="Service Features")
    training = models.CharField(max_length=10, choices=TRAININGS, null=True, blank=True, verbose_name="Training Type")

    def __str__(self):
        return self.title

    class Meta:
            verbose_name = "Service"
            verbose_name_plural = "Services"

class Player(models.Model):
    GENDERS = (("male", "Male"), ("female", "Female"))
    name = models.CharField(max_length=50, verbose_name="Player Name")
    age = models.PositiveIntegerField(default=10, validators=[MinValueValidator(10), MaxValueValidator(14)], verbose_name="Player Age")
    gender = models.CharField(max_length=6, choices=GENDERS, verbose_name="Player Gender")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name="Player")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Service")
    booking_date = models.DateTimeField(auto_now_add=True, verbose_name="Booking Date")

    def __str__(self):
        return f"{self.user.username} - {self.service.focus} - {self.player.name}"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"