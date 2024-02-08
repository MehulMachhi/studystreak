# from django.contrib import admin
# from .models import *
# from nested_admin import NestedTabularInline, NestedModelAdmin


# # Register your models here.
# admin.site.register(ReadingQuestionTypeName)
# admin.site.register(ReadingPassageName)
# # admin.site.register(Question)
# # admin.site.register()

# class OptionsInline(NestedTabularInline):
#     model = ReadingOption
#     extra = 1
    
# class QuestionInline(NestedTabularInline):
#     model = Reading_Question
#     extra = 1
#     fk_name = 'name'
#     inlines = [OptionsInline]
    
# class ReadingQuestionAdmin(NestedModelAdmin):
#     model = ReadingQuestion
#     inlines = [QuestionInline]

# admin.site.register(ReadingQuestion, ReadingQuestionAdmin)    


# '''############ Listening ##############'''   
# admin.site.register(ListeningQuestionTypeName)
# class Listening_OptionsInline(NestedTabularInline):
#     model = Listening_Options
#     extra = 1
    
# class Listening_QuestionInline(NestedTabularInline):
#     model = Listening_Question
#     extra = 1
#     fk_name = 'name'
#     inlines = [Listening_OptionsInline]
    
# class ListeningQuestionAdmin(NestedModelAdmin):
#     model = ListeningQuestion
#     inlines = [Listening_QuestionInline]

# admin.site.register(ListeningQuestion, ListeningQuestionAdmin)    
    
# '''############ Writing ##############'''   
# admin.site.register(WritingQuestionType)
# admin.site.register(WritingQuestion)     

# '''############ Writing ##############'''

# admin.site.register(SpeakingQuestion) 
# admin.site.register(SpeakingQuestionType)