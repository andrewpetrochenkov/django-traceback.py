from django.contrib import admin

from .models import Traceback

class TracebackAdmin(admin.ModelAdmin):
    list_display = ('type', 'value', 'path', '_created_at',)
    list_filter = ('type','path',)

    def _created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")
    _created_at.short_description = 'created_at'

admin.site.register(Traceback, TracebackAdmin)

