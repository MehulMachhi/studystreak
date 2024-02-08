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
    list_display = ("Name", "reading_list", "listening_list", "speaking_list", "writing_list", "module_category")
    list_filter = ("Name",)



    def reading_list(self, obj):
        return ", ".join([str(exam) for exam in obj.Reading.all()])

    def listening_list(self, obj):
        return ", ".join([str(exam) for exam in obj.Listening.all()])

    def speaking_list(self, obj):
        return ", ".join([str(exam) for exam in obj.Speaking.all()])

    def writing_list(self, obj):
        return ", ".join([str(exam) for exam in obj.Writing.all()])

    # def reading_list(self, obj):
    #     return ",".join([str(exam) for exam in obj.writing.all()])
admin.site.register(module, moduleadmin)