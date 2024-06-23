from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length= 40, null=False)
    slug = models.CharField(max_length= 40, null=False, unique=True)
    description = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False, default=0)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to="static/thumbnail")
    date = models.DateTimeField(auto_now_add=True)
    length = models.IntegerField(null=False)

    def __str__(self):
        return self.name

class CourseProperty(models.Model):
    description = models.CharField(max_length=110, null=False)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Tag(CourseProperty):
    pass

class Prerequisite(CourseProperty):
    pass

class Learning(CourseProperty):
    pass

class Video(models.Model):
    title = models.CharField(max_length=100, null=False)
    course =models.ForeignKey(Course, null = False, on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=False)
    video_id = models.CharField(max_length=30, null=False)
    is_preview = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'course')