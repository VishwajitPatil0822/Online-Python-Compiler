# Generated by Django 3.1.12 on 2025-04-10 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.BigIntegerField(blank=True, null=True)),
                ('message', models.CharField(max_length=1000)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
