# Generated by Django 4.2.13 on 2024-07-04 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football_camp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='title',
            field=models.CharField(default='Default Title', max_length=100),
            preserve_default=False,
        ),
    ]
