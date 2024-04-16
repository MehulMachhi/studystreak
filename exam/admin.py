from django.contrib import admin

from .models import Answer, Exam, SpeakingBlock, SpeakingBlockQuestion

# Register your models here.


class AnswerInline(admin.TabularInline):
    """Tabular Inline View for Answer"""

    model = Answer
    extra = 1
    fk_name = "exam"


# @admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question_number", "answer_text", "exam")
    list_filter = ("question_number", "exam")
    search_fields = ("question_number", "exam", "answer_text")

admin.site.register(Answer, AnswerAdmin)


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    search_fields = ( "exam_name",
        "block_type",
        "exam_type",
        "no_of_questions",
        "exam_category",
        "difficulty_level",
        "block_threshold",)
    list_display = [
        "exam_name",
        "block_type",
        "exam_type",
        "no_of_questions",
        "exam_category",
        "difficulty_level",
        "block_threshold",
       
    ]
    list_filter = [
        "exam_name",
        "exam_type",
        "block_type",
        "difficulty_level",
        "exam_category",
    ]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "exam_name",
                    "exam_type",
                    "exam_category",
                    "question_structure",
                ),
            },
        ),
        (
            "Block details",
            {
                "fields": (
                    "block_type",
                    "difficulty_level",
                    "block_threshold",
                ),
            },
        ),
        (
            "Question details",
            {
                "fields": (
                    "audio_file",
                    "passage",
                    'passage_image',
                    "no_of_questions",
                    "question",
                ),
            },
        ),
    )


# @admin.register(FullLengthTest)
# class FullLengthTestAdmin(admin.ModelAdmin):
#     list_display = ['test_type', 'difficulty_level', 'get_reading_exams', 'get_listening_exams', 'get_writing_exams', 'get_speaking_exams']
#     list_filter = ('test_type', 'difficulty_level')

#     def get_reading_exams(self, obj):
#         return ', '.join([exam.exam_name for exam in obj.reading.all()])

#     get_reading_exams.short_description = 'Reading Exams'

#     def get_listening_exams(self, obj):
#         return ', '.join([exam.exam_name for exam in obj.listening.all()])

#     get_listening_exams.short_description = 'Listening Exams'

#     def get_writing_exams(self, obj):
#         return ', '.join([exam.exam_name for exam in obj.writing.all()])

#     get_writing_exams.short_description = 'Writing Exams'

#     def get_speaking_exams(self, obj):
#         return ', '.join([exam.exam_name for exam in obj.speaking.all()])

#     get_speaking_exams.short_description = 'Speaking Exams'



class SpeakingAnswerInline(admin.StackedInline):
    model = SpeakingBlockQuestion
    fk_name = 'speaking_block'
    extra= 2 
@admin.register(SpeakingBlock)
class SpeakingBlockModelAdmin(admin.ModelAdmin):
    inlines = [SpeakingAnswerInline]
    list_display = ('name','block_threshold','difficulty_level','no_of_questions')

    def get_question(self,instance):
        return 'hello'