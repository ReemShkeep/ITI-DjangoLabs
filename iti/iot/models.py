from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200)
   #  trackcourses = models.ForeignKey(Track,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Track(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


class Student(models.Model):
    fname = models.CharField(max_length=50, null=False, default='first name')
    lname = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=False, default=20)
    city = models.CharField(max_length=200, null=True, default='New Capital')
    studentsTrack = models.ForeignKey(Track, on_delete=models.CASCADE)
    studentsCourse = models.ManyToManyField(Course)

    def __str__(self):
        return self.fname+' '+self.lname

    def is_graduated(self):
      if self.age>20:
         return True
      else:
         return False

    is_graduated.short_description = 'Graduated?'
    is_graduated.boolean = True
