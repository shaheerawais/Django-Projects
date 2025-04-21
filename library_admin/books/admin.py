from django.contrib import admin
from .models import Book, Review

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'is_available', 'get_year')
    list_filter = ('is_available', 'published_date')
    search_fields = ('title', 'author')
    inlines = [ReviewInline]

    def get_year(self, obj):
        return obj.published_date.year
    get_year.short_description = 'Year'

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing book
            return ['published_date']
        return []

admin.site.register(Book, BookAdmin)
admin.site.register(Review)
