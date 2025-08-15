from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Reseña, Comentario

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Información extra', {'fields': ('tipo', 'avatar', 'bio')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información extra', {'fields': ('tipo', 'avatar', 'bio')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Reseña)
admin.site.register(Comentario)