from django.shortcuts import render,redirect,get_object_or_404
from myapp.forms import StudentForm
from myapp.models import Student
# Create your views here.

def registerStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit= False)
            student.StuName = student.StuName.title()
            student.save()
            return redirect('/')
    return render(request,'myapp/register.html',{'form':form})

def getStudents(request):
    students = Student.objects.all()
    return render(request,'myapp/students.html',{'studs': students})


def getStudent(request,id):
    student = get_object_or_404(Student,id=id)
    return render(request,'myapp/find.html',{'stu':student})

def editStudent(request,id):
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'myapp/edit.html',{'form':form,'student':student})

def deleteStudent(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('/') 
    return render(request,'myapp/delete.html',{'student':student})

