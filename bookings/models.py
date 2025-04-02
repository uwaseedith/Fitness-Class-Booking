from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

class ClassSchedule(models.Model):
    title = models.CharField(max_length=100)
    trainer = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()
    capacity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='class_images/', blank=True, null=True)


    def __str__(self):
        return f"{self.title} - {self.date} {self.start_time}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} booked {self.class_schedule.title}"
