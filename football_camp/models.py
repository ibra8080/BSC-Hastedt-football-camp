from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Service Model
class Service(models.Model):
    TRAININGS = (("skills", "Skills"), ("fitness", "Fitness"), (
        "tactics", "Tactics"), ("all", "All"))
    title = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Service Title")
    focus = models.CharField(max_length=200, verbose_name="Service Focus")
    duration = models.CharField(
        max_length=100, verbose_name="Service Duration")
    features = models.TextField(verbose_name="Service Features")
    training = models.CharField(
        max_length=10,
        choices=TRAININGS,
        null=True,
        blank=True,
        verbose_name="Training Type"
    )
    image = models.ImageField(
        upload_to='services/',
        blank=True,
        null=True,
        verbose_name="Service Image"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


# Player Model
class Player(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='players')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=10, choices=[('girl', 'Girl'), ('boy', 'Boy')])
    height = models.FloatField()
    pic = models.ImageField(upload_to='players/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"


# Booking Model
class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="User")
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, verbose_name="Player")
    services = models.ManyToManyField(Service, verbose_name="Services")
    booking_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Booking Date")

    def __str__(self):
        return f"{self.user.username} - {self.player.first_name} {self.player.last_name} - {self.booking_date}"  # noqa

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"


# TrainingSchedule Model
class TrainingSchedule(models.Model):
    schedule_details = models.TextField()


# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
