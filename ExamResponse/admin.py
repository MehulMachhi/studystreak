from django.contrib import admin
from exam.models import ExamType

# Register your models here.
from .models import SpeakingResponse, Student_answer, Studentanswer


class SpeakingAnswerInline(admin.TabularInline):
    """Tabular Inline View for Answer"""

    model = SpeakingResponse
    extra = 1
    fk_name = "student_answers"


class AnswerInline(admin.TabularInline):
    """Tabular Inline View for Answer"""

    model = Student_answer
    extra = 1
    fk_name = "student_answers"


class StudentAnswerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
    )
    inlines = [AnswerInline]
    speaking_inline = [SpeakingAnswerInline]

    def get_inlines(self, request, obj):
        if obj is not None:
            if obj.exam.exam_type == ExamType.speaking:
                return self.speaking_inline
        else:
            return self.inlines

    readonly_fields = ("band",)


admin.site.register(Studentanswer, StudentAnswerAdmin)
