# Generated by Django 4.1 on 2022-08-04 00:05

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_articles_quillpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quillpost',
            name='body',
        ),
        migrations.AddField(
            model_name='quillpost',
            name='content',
            field=django_quill.fields.QuillField(default='ici'),
        ),
    ]
