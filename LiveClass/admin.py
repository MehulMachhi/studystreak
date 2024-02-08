from django.contrib import admin
from .models import Live_Class
from datetime import datetime, time, date

class LiveClassAdmin(admin.ModelAdmin):
    list_display = ['meeting_title', 'start_time', 'end_time']
    search_fields = ['meeting_title']
    ordering = ['start_time']

admin.site.register(Live_Class, LiveClassAdmin)