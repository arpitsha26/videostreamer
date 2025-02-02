# Generated by Django 5.1.3 on 2024-11-29 13:22

import player.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=500)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('video', models.FileField(upload_to='videos', validators=[player.models.validate_mp4_extension])),
                ('poster', models.ImageField(blank=True, null=True, upload_to='movie_posters/')),
                ('duration', models.PositiveIntegerField(help_text='Duration in minutes')),
                ('hls', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Completed', 'Completed')], default='Pending', max_length=20)),
                ('is_running', models.BooleanField(default=False)),
                ('categories', models.ManyToManyField(related_name='movies', to='player.category')),
                ('genres', models.ManyToManyField(related_name='movies_generes', to='player.genre')),
            ],
        ),
    ]
