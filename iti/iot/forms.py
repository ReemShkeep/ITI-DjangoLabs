from django import forms
# from iot.models import * 
from iot.models import Student,Track,Course

class StudentForm(forms.ModelForm):
    class Meta:
       model=Student
       fields='__all__'
      #  fields=['fname','lname','age','studentsTrack']

class TrackForm(forms.ModelForm):
   class Meta:
      model=Track
      fields=['name','description','courses']



class CourseForm(forms.ModelForm):
   class Meta:
      model=Course
   #  because it's tuble and if it takes one parameter 
      fields=('title',)      
      # fields=['title','description','hours']
      
   