from django.contrib import admin
from .models import Liste
from .models import Produit
from django.utils.html import format_html

@admin.register(Liste)
class ListeAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'is_shared', 'created_at', "share_token")
    list_filter = ('is_shared',)
    search_fields = ('name', 'owner__email')
    ordering = ('-created_at',)



@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('name', 'liste', 'added_by', 'is_reserved', 'reserved_by', 'price', 'image_preview')

    list_filter = ('is_reserved',)
    search_fields = ('name', 'liste__name', 'added_by__email', 'reserved_by__email')
    ordering = ('liste', 'name')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Image"
    
    
from django.contrib import admin
from .models import ShareRequest


@admin.register(ShareRequest)
class ShareRequestAdmin(admin.ModelAdmin):
    list_display = ('liste', 'invited_by', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('liste__name', 'invited_by__email')
    # readonly_fields = ('liste', 'invited_by', 'created_at')
    ordering = ('-created_at',)
