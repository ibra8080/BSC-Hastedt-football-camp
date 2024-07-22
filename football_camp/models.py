from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


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
