from django.contrib import admin

from .models import FlashCard, FlashCardItem, Gamification


class FlashCardItemInline(admin.TabularInline):
    model = FlashCardItem
    extra = 1 
    
@admin.register(FlashCard)
class FlashCardAdmin(admin.ModelAdmin):
    inlines = [FlashCardItemInline]
    list_display = ('id','course', 'title', 'description', 'set_priority',)
    
@admin.register(Gamification)
class GamificationAdmin(admin.ModelAdmin):...
    
    
    
