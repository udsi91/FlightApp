# Generated by Django 4.2.3 on 2023-07-16 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('flight_number', models.CharField(max_length=64)),
                ('airline', models.CharField(choices=[('PEG', 'Pegasus'), ('THY', 'Turkish Airlines'), ('SUN', 'Sun Expres')], max_length=3)),
                ('departure', models.PositiveSmallIntegerField(choices=[(7, 'Antalya'), (1, 'Adana'), (52, 'Ordu'), (35, 'Izmir'), (9, 'Aydın'), (10, 'Balıkesir'), (16, 'Bursa'), (32, 'Isparta'), (6, 'Ankara'), (44, 'Malatya'), (34, 'Istanbul')])),
                ('departure_date', models.DateField()),
                ('arrival', models.PositiveSmallIntegerField(choices=[(7, 'Antalya'), (1, 'Adana'), (52, 'Ordu'), (35, 'Izmir'), (9, 'Aydın'), (10, 'Balıkesir'), (16, 'Bursa'), (32, 'Isparta'), (6, 'Ankara'), (44, 'Malatya'), (34, 'Istanbul')])),
                ('arrival_date', models.DateField()),
                ('created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('0', 'Undefined'), ('M', 'Male'), ('F', 'Female')], default='0', max_length=1)),
                ('created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.flight')),
                ('passenger', models.ManyToManyField(to='flight.passenger')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
