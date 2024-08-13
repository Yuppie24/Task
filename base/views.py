from django.shortcuts import render, redirect
from .models import Student
# Create your views here.
def home(request):
    student_obj = Student.objects.all()
    context = {'Students':student_obj}
    return render(request, 'home.html', context=context)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age= request.POST.get('age')
        address = request.POST.get('address')
        grade= request.POST.get('grade')
        major= request.POST.get('major')
        Student.objects.create(name=name, age=age, address=address, grade=grade, major=major)
        return redirect(home)
    return render(request, 'create.html')

def update(request, pk ):
    student_obj = Student.objects.get(id=pk)
    context = {'student':student_obj}
    if request.method == 'POST':
        student_obj.name = request.POST.get('name')
        student_obj.age= request.POST.get('age')
        student_obj.address = request.POST.get('address')
        student_obj.grade= request.POST.get('grade')
        student_obj.major= request.POST.get('major')
        student_obj.save()
        return redirect(home)
    return render(request, 'update.html', context=context)


def delete(request, pk ):
    student_obj = Student.objects.get(id=pk)
    student_obj.delete()
    return redirect(home)