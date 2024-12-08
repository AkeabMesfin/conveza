# admin.py
from django.contrib import admin
from .models import User, SuperUser, RegularUser

# Admin for superusers only
class SuperUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'created_at')
    list_filter = ('is_staff',)
    search_fields = ('username', 'email')

    def get_queryset(self, request):
        # Show only superusers in this admin view
        qs = super().get_queryset(request)
        return qs.filter(is_superuser=True)

# Admin for regular users only
class RegularUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('username', 'email')

    def get_queryset(self, request):
        # Show only regular users (non-superusers) in this admin view
        qs = super().get_queryset(request)
        return qs.filter(is_superuser=False)

# Register both proxy models separately
admin.site.register(SuperUser, SuperUserAdmin)
admin.site.register(RegularUser, RegularUserAdmin)
