# Generated by Django 3.2.7 on 2022-06-25 04:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import weather.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update_period', models.SmallIntegerField(default=12, validators=[weather.models.validate_update_period])),
                ('town', models.CharField(blank=True, max_length=200, null=True)),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='подписчик')),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField(default=None)),
                ('feels_like', models.FloatField(default=None)),
                ('pressure', models.SmallIntegerField(default=None)),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('subscribe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='towns', to='weather.subscribe', verbose_name='подписка')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddConstraint(
            model_name='subscribe',
            constraint=models.UniqueConstraint(fields=('subscriber', 'town'), name='subscriber_town_connection'),
        ),
    ]
