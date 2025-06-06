# Generated by Django 3.1.12 on 2025-04-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_compiler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
    ]
