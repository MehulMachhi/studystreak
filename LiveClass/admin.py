from datetime import date, datetime, time
from typing import Any

from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from .models import Live_Class, LiveClassAttachment
from django.utils.html import format_html
from Courses.models import Course
from django.db.models import Q

class LiveClassAttachmentInline(admin.TabularInline):
    model= LiveClassAttachment
    extra=1

class LiveClassAdmin(admin.ModelAdmin):
    inlines = [LiveClassAttachmentInline]
    list_display = ['meeting_title', 'start_time', 'end_time', "select_batch", "liveclasstype","meeting_title", "start_time",
                    "end_time", "meeting_url"]
    search_fields = ['meeting_title']
    ordering = ['start_time']
    list_filter = ("select_batch", "liveclasstype", "meeting_title", "zoom_meeting_id", "bookslot_count", )
    search_fields = ("select_batch", "liveclasstype", "meeting_title", "zoom_meeting_id", "bookslot_count", )

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(
                Q(select_batch__add_package__select_course__tutor = request.user) |
                Q(select_batch__add_package__select_course__primary_instructor = request.user))

    def meeting_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.zoom_meeting_id)

admin.site.register(Live_Class, LiveClassAdmin)

