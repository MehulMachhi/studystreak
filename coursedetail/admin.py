import nested_admin
from django.contrib import admin
from nested_admin import NestedModelAdmin

from coursedetail.models import Quiz_Question, QuizOption
from master.models import LessonAssignment, LessonAttachment

from .models import Lesson, Note

# class LessonAssignmentInline(nested_admin.NestedStackedInline):
#     model = LessonAssignment
#     extra = 1
#     fk_name = "lesson"

#######################################################################

# class LessonAttachmentInline(nested_admin.NestedStackedInline):
#     model = LessonAttachment
#     extra = 1
#     fk_name = "lesson"


# class QuizOptionAdmin(admin.ModelAdmin):
#     model = QuizOption
#     list_display = ['name', 'Answers', 'correct_answer']
#     list_filter = ['name']
# admin.site.register(QuizOption, QuizOptionAdmin)
#     # extra = 1


# class OptionsInline(nested_admin.NestedStackedInline):
#     model = QuizOption
#     extra = 1

# class QuestionInline(nested_admin.NestedStackedInline):
#     model = Quiz_Question
#     extra = 2
#     # fk_name = 'name'
#     inlines = [OptionsInline]


# class Quiz_QuestionAdmin(NestedModelAdmin):
#     model = Lesson
#     list_display = [
#         "section",
#         "Lesson_Title",
#         "Lesson_Description",
#         "Lesson_Video",
#         "Lesson_Duration",
#         "active",
#     ]
#     list_filter = [
#         "section",
#         "Lesson_Title",
#         "Lesson_Description",
#         "Lesson_Video",
#         "Lesson_Duration",
#         "active",
#     ]
#     search_fields = ["Lesson_Title"]
#     inlines = [LessonAttachmentInline]


# admin.site.register(Lesson, Quiz_QuestionAdmin)

# class Quiz_QuestionAdmin(admin.ModelAdmin):
#     model = Lesson
#     list_display = ['Question', 'lesson',]
#     list_filter = ['Question', 'lesson',]
#     # search_fields = ['Lesson_Title']
#     # inlines = [QuestionInline]

# admin.site.register(Quiz_Question, Quiz_QuestionAdmin)

##############################################################################3

# class SiteAddressInline(admin.StackedInline):
#     model = SiteAddress


# @admin.register(Site)
# class SiteAdmin(admin.ModelAdmin):
#     inlines = [BillingAddressInline, SiteAddressInline, ContactInline]


##################################################################################

class LessonAttachmentInline(nested_admin.NestedStackedInline):
    model = LessonAttachment
    extra = 1
    fk_name = "lesson"

class OptionsInline(nested_admin.NestedStackedInline):
    model = QuizOption
    extra = 1

class QuestionInline(nested_admin.NestedStackedInline):
    model = Quiz_Question
    extra = 2
    inlines = [OptionsInline]

# class AnswerInline(admin.TabularInline):
#     """Tabular Inline View for Answer"""

#     model = Assignment_Answer
#     extra = 1
    # fk_name = "lesson"

# @admin.register(Assignment_Answer)

class LessonAdmin(NestedModelAdmin):
    model = Lesson
    list_display = [
        "section",
        "Lesson_Title",
        "Lesson_Description",
        "Lesson_Video",
        "Lesson_Duration",
        "active",
    
    ]
    list_filter = [
        "section",
        "Lesson_Title",
        "Lesson_Description",
        "Lesson_Video",
        "Lesson_Duration",
        "active",
    ]
    search_fields = ["Lesson_Title"]
    inlines = [LessonAttachmentInline, QuestionInline]

admin.site.register(Lesson, LessonAdmin)


class NoteAdmin(admin.ModelAdmin):
    list_display = ["student", "lesson",]
admin.site.register(Note,NoteAdmin)

