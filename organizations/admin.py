from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Organization, UserProfile

User = get_user_model()

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    extra = 0

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

admin.site.register(User, UserAdmin)

from .models import Organization, UserProfile, Zone
@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ("id","name","organization")
    list_filter = ("organization",)
