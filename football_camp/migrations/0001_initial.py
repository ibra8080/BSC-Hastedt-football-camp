# Generated by Django 5.0.7 on 2024-07-11 20:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Service Title')),
                ('focus', models.CharField(max_length=200, verbose_name='Service Focus')),
                ('duration', models.CharField(max_length=100, verbose_name='Service Duration')),
                ('features', models.TextField(verbose_name='Service Features')),
                ('training', models.CharField(blank=True, choices=[('skills', 'Skills'), ('fitness', 'Fitness'), ('tactics', 'Tactics'), ('all', 'All')], max_length=10, null=True, verbose_name='Training Type')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='TrainingSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('girl', 'Girl'), ('boy', 'Boy')], max_length=10)),
                ('height', models.FloatField()),
                ('pic', models.ImageField(blank=True, null=True, upload_to='players/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now_add=True, verbose_name='Booking Date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football_camp.player', verbose_name='Player')),
                ('services', models.ManyToManyField(to='football_camp.service', verbose_name='Services')),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
            },
        ),
    ]
