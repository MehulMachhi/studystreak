from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student_answer, Studentanswer

# Register your models here.





class AnswerInline(admin.TabularInline):
    """Tabular Inline View for Answer"""

    model = Student_answer
    extra = 1
    fk_name = "student_exam"

class StudentAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "user",)
    inlines = [AnswerInline]
admin.site.register(Studentanswer, StudentAnswerAdmin)