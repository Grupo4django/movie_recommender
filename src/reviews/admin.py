from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie', 'user', 'rating', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'created_at', 'rating')
    search_fields = ('title', 'content', 'user__username', 'movie__title')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)
    approve_reviews.short_description = "Approve selected reviews"
