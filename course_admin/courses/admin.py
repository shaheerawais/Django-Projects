from django.contrib import admin
from .models import Instructor, Course

# Show inline courses on instructor page
class CourseInline(admin.TabularInline):
    model = Course
    extra = 1  # show 1 blank form

# Custom Course admin
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'start_date', 'is_active', 'get_year')
    list_filter = ('is_active', 'start_date')
    search_fields = ('title', 'instructor__name')

    def get_year(self, obj):
        return obj.start_date.year
    get_year.short_description = 'Year'

    def get_readonly_fields(self, request, obj=None):
        return ['start_date']

# Custom Instructor admin
class InstructorAdmin(admin.ModelAdmin):
    inlines = [CourseInline]

# Register both with custom classes
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Course, CourseAdmin)
