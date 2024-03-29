# Generated by Django 4.1 on 2023-12-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(default=0)),
                ('player_name', models.CharField(max_length=200)),
                ('player_title', models.CharField(choices=[(' ', ' '), ('CM', 'CM'), ('FM', 'FM'), ('IM', 'IM'), ('GM', 'GM')], default=' ', max_length=10)),
                ('player_rating', models.IntegerField(default=0)),
                ('age', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name_plural': 'ratings',
            },
        ),
        migrations.CreateModel(
            name='RatingsWorld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(default=0)),
                ('player_name', models.CharField(max_length=200)),
                ('player_title', models.CharField(choices=[(' ', ' '), ('CM', 'CM'), ('FM', 'FM'), ('IM', 'IM'), ('GM', 'GM')], default=' ', max_length=10)),
                ('player_rating', models.IntegerField(default=0)),
                ('age', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name_plural': 'world_ratings',
            },
        ),
    ]
