from django.contrib import admin
from .models import Category, Genre, Movie
# Register your models here.

admin.site.register(Category)
admin.site.register(Genre)

class MovieAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Movie._meta.get_fields()
                    if not (field.many_to_many or field.one_to_many)]

admin.site.register(Movie,MovieAdmin)





