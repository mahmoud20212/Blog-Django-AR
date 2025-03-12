from django.contrib import admin
from .models import Post, Comment, About, Setting


admin.site.register(Setting)
admin.site.register(About)
admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author']
    list_filter = ['post_date', 'author']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    # date_hierarchy = 'post_date'
    # ordering = ['status', 'publish']