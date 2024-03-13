from django.contrib import admin
from .models import Live_Class
from datetime import datetime, time, date

class LiveClassAdmin(admin.ModelAdmin):
    list_display = ['meeting_title', 'start_time', 'end_time']
    search_fields = ['meeting_title']
    ordering = ['start_time']
    list_filter = ("select_batch", "liveclasstype", "meeting_title", "zoom_meeting_id", "bookslot_count", )
    search_fields = ("select_batch", "liveclasstype", "meeting_title", "zoom_meeting_id", "bookslot_count", )

admin.site.register(Live_Class, LiveClassAdmin)