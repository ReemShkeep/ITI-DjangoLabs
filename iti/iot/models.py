from django.db import models

# Create your models here.
class Track(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name
     
     
class Student(models.Model):
    fname = models.CharField(max_length=50,null=True,default='first name')
    lname = models.CharField(max_length=50,null=True,default='last Name')
    age = models.IntegerField()
    city = models.CharField(max_length=200,null=True,default='New Capital')
    studensTrack = models.ForeignKey(Track,on_delete=models.CASCADE)
    def __str__(self):
        return self.name   