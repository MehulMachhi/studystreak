from django.contrib import admin
from exam.models import ExamType

# Register your models here.
from .models import SpeakingResponse, Student_answer, Studentanswer, SpeakingBlockAnswer


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
        "exam",
        "Practise_Exam",
        "Full_Length_Exam",
        "band",
        "exam_type"
       
    )
    list_filter = ("exam", "user", "Practise_Exam", "Full_Length_Exam", "AI_Assessment", "Tutor_Assessment", "band", "exam_type")
    search_fields = ("exam", "user", "Practise_Exam", "Full_Length_Exam", "AI_Assessment", "Tutor_Assessment", "band", "exam_type")
    inlines = [AnswerInline]
    speaking_inline = [SpeakingAnswerInline]

    # def get_inlines(self, request, obj):
    #     if obj:
    #         if obj.exam.exam_type == ExamType.speaking:
    #             return self.speaking_inline
    #     return super().get_inlines(request, obj)

    # readonly_fields = ("band",)


admin.site.register(Studentanswer, StudentAnswerAdmin)


@admin.register(SpeakingBlockAnswer)
class SpeakingResponseModelAdmin(admin.ModelAdmin):
    pass
