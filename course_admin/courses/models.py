from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    joined_date = models.DateField()

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    start_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
