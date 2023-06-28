from django.contrib import admin
from .models import *


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'category' , 'first_name', 'email', 'specialization','institute', 'gender', 'address', 'password']
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


