# Generated by Django 4.1 on 2022-08-08 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_tournaments_options_tournaments_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournaments',
            name='ends',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournaments',
            name='starts',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]