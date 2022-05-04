from django.contrib import admin
from .models import ScUser


@admin.register(ScUser)
class ScUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'post', 'department')
    list_display_links = ('username', 'full_name', )
    search_fields = 'full_name',
    list_filter = ('department',)
    readonly_fields = ('updated', 'username', 'first_name', 'last_name', 'full_name',
                       'post', 'department')

    fieldsets = (
        (None, {'fields': ('email', 'full_name',)}),
        ('Основные данные', {'fields': ('username', 'first_name', 'last_name',
                                'post', 'department')}),
        ('Поледний вход', {'fields': ('updated',)}),
    )
