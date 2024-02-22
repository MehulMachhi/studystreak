from django.contrib import admin

from .models import createexam, module

# Register your models here.


class createexamadmin(admin.ModelAdmin):
    list_display = ("id", "ielts_names")

    def ielts_names(self, obj):
        return str(obj.IELTS.Name) if obj.IELTS else ""


admin.site.register(createexam, createexamadmin)
# admin.site.register(Responses)


class moduleadmin(admin.ModelAdmin):
    list_display = (
        "Name",
        "reading_list",
        "listening_list",
        "speaking_list",
        "writing_list",
        "a_w_a_list",
        "integrated_reasoning_list",
        "quantitative_reasoning_list",
        "verbal_reasoning_list",
    )
    list_filter = ("Name",)

    def reading_list(self, obj):
        return ", ".join([str(exam) for exam in obj.Reading.all()])

    def listening_list(self, obj):
        return ", ".join([str(exam) for exam in obj.Listening.all()])

    def speaking_list(self, obj):
        return ", ".join([str(exam) for exam in obj.Speaking.all()])

    def writing_list(self, obj):
        return ", ".join([str(exam) for exam in obj.Writing.all()])
    
    
    def a_w_a_list(self, obj):
        return self.display_related_exams(obj.a_w_a.all())
    
    def integrated_reasoning_list(self, obj):
        return self.display_related_exams(obj.integrated_reasoning.all())
    
    def quantitative_reasoning_list(self, obj):
        return self.display_related_exams(obj.quantitative_reasoning.all())
    
    def verbal_reasoning_list(self, obj):
        return self.display_related_exams(obj.verbal_reasoning.all())

    def display_related_exams(self, exams):
        return ", ".join([str(exam) for exam in exams]) if exams.exists() else "-"

    # def reading_list(self, obj):
    #     return ",".join([str(exam) for exam in obj.writing.all()])


admin.site.register(module, moduleadmin)
