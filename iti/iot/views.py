from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from iot.models import Student,Track ,Course
from iot.forms import StudentForm,TrackForm,CourseForm


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



def newStudent(request):
   stForm=StudentForm()   #this is an empty form the above is save the form 
   if request.method=='POST':
      stForm=StudentForm(request.POST)
      if stForm.is_valid():
         stForm.save()
         # return HttpResponse('Student Added Successfully')
         # it takes me the url and hit the function of it 
         return HttpResponseRedirect(redirect_to='/iot/allstu/')
   context={'st_form' : stForm}
   return render(request,'iot/newstudent.html', context)



def editStudent(request,st_id):
   st=Student.objects.get(id=st_id)
   stForm=StudentForm(instance=st)
   if request.method=='POST':
      stForm=StudentForm(request.POST,instance=st)
      if stForm.is_valid():
         stForm.save()
         return HttpResponseRedirect(redirect_to='/iot/allstu/')
   context={'st_form' : stForm}
   return render(request,'iot/newstudent.html', context)



def deleteStudent(request,st_id):
   st=Student.objects.get(id=st_id)
   # if request.method=='POST':
   st.delete()
   return HttpResponseRedirect(redirect_to='/iot/allstu/') 