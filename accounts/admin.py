from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.


UserAdmin.list_display = ('username', 'email')

admin.site.register(User, UserAdmin)
