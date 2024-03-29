# Generated by Django 4.2 on 2023-05-01 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='Tournaments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail_t', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('description', django_quill.fields.QuillField()),
                ('starts', models.DateField()),
                ('ends', models.DateField()),
                ('ratingType', models.CharField(choices=[(' ', ' '), ('FIDE Rated', 'FIDE Rated'), ('Chess SA Rated', 'Chess SA Rated'), ('Not Rated', 'Not Rated')], default=' ', max_length=100)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('featured_tournament', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'verbose_name_plural': 'tournaments',
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.TextField(blank=True, max_length=500, null=True)),
                ('body', django_quill.fields.QuillField()),
                ('slug', models.SlugField(blank=True, max_length=300)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('featured_article', models.BooleanField(blank=True, default=False, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'articles',
            },
        ),
    ]
