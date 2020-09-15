from django.contrib import admin
from .models import Article
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Article._meta.fields if field.name != 'description']
