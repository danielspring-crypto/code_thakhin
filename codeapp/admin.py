from django.contrib import admin
from .models import Python

class PythonAdmin(admin.ModelAdmin):
	list_display = ['title', 'author', 'date']
	list_filter = ['author', 'date']

admin.site.register(Python, PythonAdmin)