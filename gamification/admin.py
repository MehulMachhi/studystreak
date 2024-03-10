from django.contrib import admin

from .models import Badge, FlashCard, FlashCardItem, Gamification, PointHistory


class FlashCardItemInline(admin.TabularInline):
    model = FlashCardItem
    extra = 1 
    
@admin.register(FlashCard)
class FlashCardAdmin(admin.ModelAdmin):
    inlines = [FlashCardItemInline]
    list_display = ('id','course', 'title', 'description', 'set_priority',)
    
@admin.register(Gamification)
class GamificationAdmin(admin.ModelAdmin):...
    
    
@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):...
    

@admin.register(PointHistory)
class PointHistoryAdmin(admin.ModelAdmin):...
    
