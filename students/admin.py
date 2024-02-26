# students/admin.py

import json

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.template.response import TemplateResponse
from import_export.admin import ExportMixin

from .models import Student


class StudentAdmin(ExportMixin, admin.ModelAdmin):
    ordering = ("-created_at",)
    date_hierarchy = "created_at"

    # def changelist_view(self, request, extra_content=None):
    #     response = super().changelist_view(request, extra_context=extra_content)
    #     queryset = response.context_data["cl"].queryset
    #     chart_data = self.chart_data(queryset)
    #     as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
    #     response.context_data.update({"chart_data": as_json})
    #     return response

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            if isinstance(response, TemplateResponse):
                queryset = response.context_data["cl"].queryset
                chart_data = self.chart_data(queryset)
                as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
                response.context_data.update({"chart_data": as_json})
        except KeyError:
            pass
        return response

    def chart_data(self, queryset):
        return (
            queryset.annotate(date=TruncDay("created_at"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

    import_export_change_list_template = (
        "admin/students/student/change_list_export.html"
    )
    list_display = (
        "first_name",
        "last_name",
        "whatsapp_no",
        "last_education",
        "ielts_taken_before",
        "duolingo_taken_before",
        "pte_taken_before",
        "toefl_taken_before",
        "country_interested_in",
        "remark",
        'get_batch_names',
        "interested_in_visa_counselling",
        "referal_code",
    )

    fieldsets = (
    (
        "Registration",
        {
            "fields": (
                "user",
                "gender",
                "country",
                "state",
                "city",
                "phone_no",
                "whatsapp_no",
                "reference_by",
            )
        },
    ),
    (
        "Profile",
        {
            "fields": (
                "country_interested_in",
                "Live_class_enroll",
                "last_education",
                "ielts_taken_before",
                "duolingo_taken_before",
                "pte_taken_before",
                "toefl_taken_before",
                "gre_taken_before",
                "gmat_taken_before",
                "remark",
                "biography",
                "user_image",
                "interested_in_visa_counselling",
                "select_batch",
                "select_package",
                "referal_code",
            ),
        },
    ),
    (
        "Counter",
        {
            "fields": (
                "student_mock_test",
                "student_pt_flt",
            ),
        },
    ),
)

    def get_batch_names(self, obj):
        return ", ".join([batch.batch_name for batch in obj.select_batch.all()])
        get_batch_names.short_description = 'Batch Names'

    admin.display(empty_value="???")

    def first_name(self, obj):
        return obj.user.first_name if obj.user.first_name else "--"

    def last_name(self, obj):
        return obj.user.last_name if obj.user.first_name else "--"

    empty_value_display = "-empty-"
    list_filter = [
        "gender",
        "country_interested_in",
        "state",
        "city",
        "ielts_taken_before",
        "duolingo_taken_before",
        "pte_taken_before",
        "toefl_taken_before",
        "gre_taken_before",
        "gmat_taken_before",
        "interested_in_visa_counselling",
        "select_batch",
    ]

    search_fields = (
        "user__first_name",
        "user__last_name",
    )
    readonly_fields = ("referal_code",)
 
admin.site.register(Student, StudentAdmin)


