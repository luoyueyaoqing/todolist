from django.contrib import admin
from .models import Todo, User


admin.site.register(Todo)
admin.site.register(User)