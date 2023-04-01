from django.contrib import admin
from .models import Student, Track, Course
# Register your models here.
class CustomStudent(admin.ModelAdmin):
   fieldsets = (
      ["Student Information", {"fields": ["fname","lname","age","city"]}],
      ["Scholarship Information", {"fields": ["studentsTrack", "studentsCourse"]}]
       )
   # def students(self, obj):
   #     return obj.students.fname



# to make the studentsCourse and studentsTrack in the admin page
# using inline to make the student could be inherted in the track and course panel 
#lma agy a3ml add for the track a2dr a3ml add for the students too

class inlineStudent(admin.StackedInline):
   model = Student
   extra = 3    
class CustomTrack(admin.ModelAdmin):
   inlines=[inlineStudent]
   
   
   
   #How lw 3aiza a2semha fieldsets m3 l inline
   # fieldsets = (["Track Information",{"fields": ("name","description","courses" )}])
            #  ["Student Information", {"fields": (" inlines=[inlineStudent]",)}])
   # def studentsTrack(self, obj):
   #     return obj.studentsTrack.name
    
class CustomCourse(admin.ModelAdmin):
      def studentsCourse(self, obj):
          return obj.studentsCourse.title
   
admin.site.register(Student, CustomStudent)
admin.site.register(Track, CustomTrack)
admin.site.register(Course, CustomCourse)
 