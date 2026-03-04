from django.contrib import admin
from .models import Category, Tag, Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'created_at')
    list_filter = ('category', 'user')
    search_fields = ('title', 'content')

admin.site.register(Category)
admin.site.register(Tag)