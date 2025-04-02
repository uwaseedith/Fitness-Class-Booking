from django.contrib import admin
from .models import ClassSchedule, Booking, UserProfile

@admin.register(ClassSchedule)
class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'trainer', 'date', 'start_time', 'end_time', 'capacity')

admin.site.register(Booking)
admin.site.register(UserProfile)
