from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

from .models import Article

class CommentInline(admin.TabularInline):
    model = models.Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment)

