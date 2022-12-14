# Generated by Django 4.1 on 2022-08-06 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_articles_delete_quillpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=200)),
                ('player_title', models.CharField(choices=[(' ', ' '), ('CM', 'CM'), ('FM', 'FM'), ('IM', 'IM'), ('GM', 'GM')], default=' ', max_length=10)),
                ('player_rating', models.IntegerField(default=0)),
                ('region', models.CharField(max_length=100)),
            ],
        ),
    ]
