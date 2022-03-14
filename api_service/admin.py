from django.contrib import admin
from .models import School, Student


class StudentAdminInline(admin.TabularInline):
    model = Student
    fields = ['first_name', 'last_name']
    extra = 0


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    inlines = (StudentAdminInline,)

    # This is for creating a list column of how many students available in the school instance
    def student_count_display(self, obj: School) -> int:
        return len(obj.students.all())

    student_count_display.short_description = 'Number of Registered Students'
    list_display = ['name', 'location', 'max_student_capacity', 'student_count_display']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'school']
