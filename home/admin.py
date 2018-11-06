from django.contrib import admin
from home.models import Social, Settings, About


@admin.register(Social)
class SeminarInline(admin.ModelAdmin):
    ordering = ('pk',)
    list_display = ('name', 'enabled', 'url')


@admin.register(Settings)
class SeminarInline(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(About)
class SeminarInline(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
