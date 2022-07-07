from datetime import date

from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Category', max_length=200)
    description = models.TextField('Description')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'


class Character(models.Model):
    name = models.CharField('Name', max_length=100)
    age = models.PositiveSmallIntegerField('Age', default=0)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='character/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('character_detail', kwargs={'slug': self.name})

    class Meta:
        verbose_name = 'Character and author'
        verbose_name_plural = 'Character and author'


class Genre(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genre'


class Anime(models.Model):
    title = models.CharField('Title', max_length=100)
    tagline = models.CharField('Slogan', max_length=100)
    description = models.TextField('Description')
    poster = models.ImageField('Poster', upload_to='anime/')
    year = models.PositiveSmallIntegerField('Date of published', default=2022)
    country = models.CharField('Country', max_length=30)
    author = models.ManyToManyField(Character, verbose_name='Author', related_name='anime_author')
    character = models.ManyToManyField(Character, verbose_name='character', related_name='anime_character')
    genres = models.ManyToManyField(Genre, verbose_name='genres')
    premier = models.DateField('Premier', default=date.today)
    budget = models.PositiveIntegerField('Budget', default=0, help_text='enter the amount in dollars')
    fees_in_japan = models.PositiveIntegerField('Fees in Japan', default=0, help_text='enter the amount in dollars')
    fees_in_world = models.PositiveIntegerField('Fees in World', default=0, help_text='enter the amount in dollars')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField('Draft', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('anime_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Anime'
        verbose_name_plural = 'Anime'


class AnimeFootage(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='anime-footage/')
    anime = models.ForeignKey(Anime, verbose_name='Anime', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Anime footage'
        verbose_name_plural = 'Anime footage'


class RatingStar(models.Model):
    value = models.SmallIntegerField('Value', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Rating star'
        verbose_name_plural = 'Rating stars'


class Rating(models.Model):
    ip = models.CharField('IP address', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='star')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, verbose_name='anime')

    def __str__(self):
        return f'{self.star} - {self.anime}'

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Name', max_length=100)
    text = models.TextField('text', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Parent', on_delete=models.SET_NULL, blank=True, null=True)
    anime = models.ForeignKey(Anime, verbose_name='Anime', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.anime}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
