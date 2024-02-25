# Courses/admin.py

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from master.models import AdditionalResource, CourseMaterial

from .models import Course, YoutubeDataRecord


@admin.register(YoutubeDataRecord)
class YoutubeDataRecordAdmin(admin.ModelAdmin):...
    

class CourseMaterialInline(admin.TabularInline):
    model = CourseMaterial
    extra = 1


class AdditionalResourceInline(admin.TabularInline):
    model = AdditionalResource
    extra = 1


@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    inlines = [CourseMaterialInline, AdditionalResourceInline]
    list_display = [
        "Course_Title",
        "Category",
        "Level",
        "Language",
        "EnrollmentStartDate",
        "EnrollmentEndDate",
        "is_active",
        "Featured",
        "Support_Available",
        "faqs",
        "Course_Overview_Provider",
        "Course_Overview_URL",
        "Course_Thumbnail",
        "SEO_Meta_Keywords",
        "Meta_Description",
    ]
    list_filter = (
        "Course_Title",
        "Category",
        "Level",
        "Language",
        "EnrollmentStartDate",
        "EnrollmentEndDate",
        "is_active",
        "faqs",
        "Featured",
        "Support_Available",
        "Course_Overview_Provider",
        "lessons",
    )
    filter_horizonal = ("lessons",)
    search_fields = [
        "Course_Title",
        "Short_Description",
        "Description",
        "Category",
        "Level",
        "Language",
        "EnrollmentStartDate",
        "EnrollmentEndDate",
        "is_active",
        "faqs",
    ]

    fieldsets = (
        (
            "Course Detail",
            {
                "fields": (
                    "Course_Title",
                    "course_identifier",
                    "Short_Description",
                    "Description",
                    "Category",
                    "Level",
                    "Language",
                    "EnrollmentStartDate",
                    "EnrollmentEndDate",
                    "max_enrollments",
                    "Featured",
                    "Support_Available",
                    "course_type",
                    "course_delivery",
                    "primary_instructor",
                    "is_active",
                    "faqs",
                    "tutor",
                )
            },
        ),
        (
            "Requirements",
            {
                "fields": ("Requirements",),
            },
        ),
        (
            "Outcome",
            {
                "fields": ("Outcome",),
            },
        ),
        (
            "Course Media",
            {
                "fields": (
                    "Course_Overview_Provider",
                    "Course_Overview_URL",
                    "Course_Thumbnail",
                ),
            },
        ),
        (
            "Course SEO",
            {
                "fields": (
                    "SEO_Meta_Keywords",
                    "Meta_Description",
                ),
            },
        ),
        (
            "Lesson",
            {
                "fields": ("lessons",),
            },
        ),
    )


# admin.site.register()
