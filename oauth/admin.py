from django.contrib import admin
from oauth.models import Profile, Oauth


@admin.register(Profile)
class SeminarInline(admin.ModelAdmin):
    ordering = ('-pk',)
    list_display = ('user', 'email_verified', 'twitch_id')

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Oauth)
class SeminarInline(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
