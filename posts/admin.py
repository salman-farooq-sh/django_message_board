from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'publication_date')
    search_fields = ['text']
    list_filter = ['publication_date']
    ordering = ['-publication_date']


admin.site.register(Post, PostAdmin)
