from django.contrib import admin
from django import forms
from .models import MovieShots, Actor, Category, Genre, Movie, RaitingStar, Reviews, Raiting
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


class MovieShotsInLine(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='150' height='100'>")

    get_image.short_description = "Изображение"

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [MovieShotsInLine, ReviewInline]
    save_on_top = True
    actions = ["publish", "unpublish"]
    save_as = True
    form = MovieAdminForm
    readonly_fields = ("get_image",)
    list_editable = ("draft",)
    #fields = (("actors", "directors", "genres"), )
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"), )
        }),
        (None, {
            "fields": ("description", ("poster", "get_image"))
        }),
        (None, {
            "fields": (("year", "world_primier", "country"), )
        }),
    )

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.poster.url} width='300' height='300'>")

    get_image.short_description = "Постер"

    def unpublish(self, request, queryset):
        """Unpublished"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else: 
            message_bit = f"{row_update} записей были обновлены" 
        self.message_user(request, f"{message_bit}")
    
    def publish(self, request, queryset):
        """Published"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else: 
            message_bit = f"{row_update} записей были обновлены" 
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permission = ('change',)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permission = ('change',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "id")
    list_display_links = ("name",)


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")
    

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image")

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='50' height='60'>")

    get_image.short_description = "Изображение"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "url")


@admin.register(RaitingStar)
class RaitingstarAdmin(admin.ModelAdmin):
    list_display = ("value",)


@admin.register(Raiting)
class RaitingAdmin(admin.ModelAdmin):
    list_display = ("ip", "star", "movie")


@admin.register(MovieShots)
class MovieshotsAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image", "movie")

admin.site.site_title = "Django Movies"
admin.site.site_header = "Django Movies"