from django.contrib import admin

from .models import Badge, FlashCard, FlashCardItem, Gamification, PointHistory


class FlashCardItemInline(admin.TabularInline):
    model = FlashCardItem
    extra = 1 
    
@admin.register(FlashCard)
class FlashCardAdmin(admin.ModelAdmin):
    inlines = [FlashCardItemInline]
    list_display = ('id','course', 'title', 'description', 'set_priority',)
    list_filter = ("course", "title", "set_priority",)
    search_fields = ("course", "title", "set_priority",)

@admin.register(Gamification)
class GamificationAdmin(admin.ModelAdmin):
    list_filter = ("content_type", "object_id", "points",)
    search_fields = ("content_type", "object_id", "points",)
    
    
@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_filter = ("title", "points_required", "gamification_items","next_badge",)
    search_fields = ("title", "points_required", "gamification_items","next_badge",)
    

@admin.register(PointHistory)
class PointHistoryAdmin(admin.ModelAdmin):
    list_filter = ("student", "gamification",)
    search_fields = ("student", "gamification",)
    
