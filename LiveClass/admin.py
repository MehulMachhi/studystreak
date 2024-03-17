from datetime import date, datetime, time

from django.contrib import admin

from .models import Live_Class, Note


class LiveClassAdmin(admin.ModelAdmin):
    list_display = ['meeting_title', 'start_time', 'end_time']
    search_fields = ['meeting_title']
    ordering = ['start_time']
    list_filter = ("select_batch", "liveclasstype", "meeting_title", "zoom_meeting_id", "bookslot_count", )
    search_fields = ("select_batch", "liveclasstype", "meeting_title", "zoom_meeting_id", "bookslot_count", )

admin.site.register(Live_Class, LiveClassAdmin)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):...
    
