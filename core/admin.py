from django.contrib import admin
from .models import Post

# from .forms import (
#     CustomUserCreationForm,
#     CustomUserChangeForm
# )
# from django.contrib.auth.admin import UserAdmin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'titulo', 'conteudo', 'estado', 'categorias']
    

# Register your models here.
# @admin.register(Post)

"""
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Post
    list_display = [
        'registro',
    ]
    fieldsets = [
        [
            None,
            {
                'fields': [
                    'password',
                ]
            }
        ],
        [
            'Personal Information',
            {
                'fields': [
                ]
            }
        ],
        [
            'Permissions',
            {
                'fields': [
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions'
                ]
            }
        ],
        [
            'Important Dates',
            {
                'fields': [
                    'last_login',
                    'date_joined'
                ]
            }
        ]
    ]
"""