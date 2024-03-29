from django.contrib import admin

from .models import Song

# Register your models here.

class SongAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    prepopulated_fields = {'slug': ('title')}


admin.site.register(Song, SongAdmin)