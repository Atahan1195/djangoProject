# Generated by Django 5.0.1 on 2024-02-01 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
    ]
