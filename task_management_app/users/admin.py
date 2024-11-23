from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import OAuthSettings

@admin.register(OAuthSettings)
class OAuthSettingsAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'created_at', 'updated_at')