from django.contrib import admin

from .models import CoursesData

class AdminCoursesData(admin.ModelAdmin):
    list_display = ['course_id',
                    'course_name',
                    'course_dur',
                    'start_date',
                    'start_time',
                    'trainer_name',
                    'trainer_experiance']


admin.site.register(CoursesData,AdminCoursesData)
