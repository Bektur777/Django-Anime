from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AnimeAdminForm(forms.ModelForm):
    description = forms.CharField(label='Descriptionn', widget=CKEditorUploadingWidget())

    class Meta:
        model = Anime
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


class AnimeFootageInline(admin.TabularInline):
    model = AnimeFootage
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="auto">')

    get_image.short_description = 'Image'


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [AnimeFootageInline, ReviewInline]
    actions = ['publish', 'unpublish']
    save_on_top = True
    save_as = True
    form = AnimeAdminForm
    list_editable = ('draft',)
    readonly_fields = ('get_image',)
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'), )
        }),
        (None, {
            'fields': (('description', 'poster', 'get_image'),)
        }),
        (None, {
            'fields': ('year', 'premier', 'country'),
        }),
        ('Them', {
            'classes': ('collapse', ),
            'fields': (('character', 'author', 'genres', 'category'),)
        }),
        (None, {
            'fields': (('budget', 'fees_in_japan', 'fees_in_world'),)
        }),
        ('Options', {
            'fields': (('url', 'draft'),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="auto">')

    get_image.short_description = 'Poster'

    def publish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = 'Была добавлена 1 запись'
        else:
            message_bit = f'{row_update} записей были добавлены'
        self.message_user(request, f'{message_bit}')

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = 'Была обновлена 1 запись'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')

    publish.short_description = 'Опубликовать'
    publish.allowed_permissions = ('change',)

    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permissions = ('change',)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'parent', 'anime')
    list_display_links = ('name', )
    readonly_fields = ('email', 'name',)


@admin.register(AnimeFootage)
class AnimeFootage(admin.ModelAdmin):
    list_display = ('title', 'anime', 'id', 'get_image')
    readonly_fields = ('get_image',)
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="60" height="auto">')

    get_image.short_description = 'Image'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = 'Image'


@admin.register(Rating)
class Rating(admin.ModelAdmin):
    list_display = ('anime', 'star', 'ip')


admin.site.register(RatingStar)

admin.site.site_title = 'Django Admin'
admin.site.site_header = 'Django Admin'
