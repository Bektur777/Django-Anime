# Generated by Django 4.0.5 on 2022-06-30 06:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('tagline', models.CharField(max_length=100, verbose_name='Slogan')),
                ('description', models.TextField(verbose_name='Description')),
                ('poster', models.ImageField(upload_to='anime/', verbose_name='Poster')),
                ('year', models.PositiveSmallIntegerField(default=2022, verbose_name='Date of published')),
                ('country', models.CharField(max_length=30, verbose_name='Country')),
                ('premier', models.DateField(default=datetime.date.today, verbose_name='Premier')),
                ('budget', models.PositiveIntegerField(default=0, help_text='enter the amount in dollars', verbose_name='Budget')),
                ('fees_in_japan', models.PositiveIntegerField(default=0, help_text='enter the amount in dollars', verbose_name='Fees in Japan')),
                ('fees_in_world', models.PositiveIntegerField(default=0, help_text='enter the amount in dollars', verbose_name='Fees in World')),
                ('url', models.SlugField(max_length=150, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Draft')),
            ],
            options={
                'verbose_name': 'Anime',
                'verbose_name_plural': 'Anime',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Category')),
                ('description', models.TextField(verbose_name='Description')),
                ('url', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Age')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='character/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Character and author',
                'verbose_name_plural': 'Character and author',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('url', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genre',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Rating star',
                'verbose_name_plural': 'Rating stars',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('text', models.TextField(max_length=5000, verbose_name='text')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.anime', verbose_name='Anime')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='anime.reviews', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP address')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.anime', verbose_name='anime')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.ratingstar', verbose_name='star')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
        migrations.CreateModel(
            name='AnimeFootage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='anime-footage/', verbose_name='Image')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.anime', verbose_name='Anime')),
            ],
            options={
                'verbose_name': 'Anime footage',
                'verbose_name_plural': 'Anime footage',
            },
        ),
        migrations.AddField(
            model_name='anime',
            name='author',
            field=models.ManyToManyField(related_name='anime_author', to='anime.character', verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='anime',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='anime.category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='anime',
            name='character',
            field=models.ManyToManyField(related_name='anime_character', to='anime.character', verbose_name='character'),
        ),
        migrations.AddField(
            model_name='anime',
            name='genres',
            field=models.ManyToManyField(to='anime.genre', verbose_name='genres'),
        ),
    ]
