from django.contrib import admin
from .models import Banner

# Register your models here.
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden', 'activo')
    list_editable = ('orden', 'activo')