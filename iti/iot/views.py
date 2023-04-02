from django.shortcuts import render
from django.http import HttpResponse
from iot.models import Student,Track ,Course

# Create your views here.
def home(request):
     return HttpResponse ('<h1>Hello This is Home Page</h1> ')
   #  return render(request, 'iot/home.html')

# http response ka2ny b3ml print 3l console lakn render ka2ny bktp f file bysm3 3shan a3ml render 3la html page
def getStudent(request, st_id):
   st=Student.objects.get(id=st_id)
   context={'student':st}
   return render(request,'iot/student.html', context)
   # return HttpResponse ('<h1>Hello This is The Student Page of Student No.'  + st_id + '<h1> and his name is '+ st.fname + ' ' + st.lname)


def getAllStudents(request):
   allStudents=Student.objects.all()
   # esm l variable eli hyru7 ll template wl value asln bta3u eli gebtu fl variable eli fu2 
   context={'students':allStudents}
   return render(request,'iot/allstudents.html', context)
   # return render(request, 'iot/allstudents.html', {'students':allStudents})
