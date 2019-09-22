from django.shortcuts import render, redirect
from .models import *

def home(request):
    return render(request, 'index.html')

def department(request): #department_add is written with this view itself
    if request.method=='POST':
        name = request.POST['name']
        code = request.POST['code']
        hod = request.POST['hod']
        dept = Department()
        dept.name = name
        dept.code = code
        dept.hod = hod
        dept.save()
        department = Department.objects.all()
        return render(request, 'department.html', {'departments': department})
    else:
        department = Department.objects.all()
        return render(request, 'department.html', {'departments': department})

def department_edit(request, pk):
    if request.method=='POST':
        id = request.POST['id']
        name = request.POST['name']
        code = request.POST['code']
        hod = request.POST['hod']
        dept = Department.objects.get(id=id)
        dept.name = name
        dept.code = code
        dept.hod = hod
        dept.save()
        return redirect('department')
    else:
        dept_to_edit = Department.objects.get(id=pk)
        department = Department.objects.all()
        return render(request, 'department.html', {'departments': department, 'dept_to_edit':dept_to_edit})
    

def department_delete(request, pk):
    dept = Department.objects.get(id=pk)
    dept.delete()
    return redirect('department')






def course(request):                #course_add is written with this view itself
    if request.method=='POST': 
        dept_id = request.POST['dept_id']
        name = request.POST['name']
        code = request.POST['code']

        crs = Course()
        crs.name=name
        crs.c_id=code
        crs.department=Department.objects.get(id=dept_id)
        crs.save()

        department = Department.objects.all().order_by('name')
        course = Course.objects.all()
        return render(request, 'course.html', {'courses':course,'departments':department})
    else:
        course = Course.objects.all()
        department = Department.objects.all()
        return render(request, 'course.html', {'courses':course,'departments':department})

def course_edit(request, pk):
    if request.method=='POST': 
        dept_id = request.POST['dept_id']
        name = request.POST['name']
        code = request.POST['code']

        crs = Course.objects.get(id=pk)
        crs.name=name
        crs.c_id=code
        crs.department=Department.objects.get(id=dept_id)
        crs.save()

        department = Department.objects.all()
        course = Course.objects.all()
        return redirect('course')
    else:
        course = Course.objects.all()
        course_to_edit=Course.objects.get(id=pk)
        department = Department.objects.all()
        return render (request,'course.html', {'courses':course,'course_to_edit':course_to_edit,'departments':department})
    
def course_delete(request, pk):
    department = Course.objects.get(id=pk)
    department.delete()
    return redirect('course')

def semester(request):
    if request.method=='POST':     
        sem = Semester()
        sem.academic_year = AcademicYear.objects.get(id = request.POST['academic_year'])
        sem.number = request.POST['semester']
        sem.course_id = request.POST['course_id']
        sem.from_date = request.POST['from']
        sem.to_date = request.POST['to']
        sem.name = 'Semester - ' + request.POST['semester']
        sem.save()
        course = Course.objects.all()
        semester = Semester.objects.all()
        academic_year = AcademicYear.objects.all()
        return render(request,'semester.html',{'semesters':semester,'courses':course, 'academic_years':academic_year})
    else:
        semester = Semester.objects.all()
        course = Course.objects.all()
        academic_year = AcademicYear.objects.all()
        return render(request,'semester.html',{'semesters':semester,'courses':course, 'academic_years':academic_year})

def semester_edit(request,pk):
    if request.method=='POST': 
        sem = Semester.objects.get(id=pk)
        sem.number = request.POST['semester']
        sem.course_id = request.POST['course_id']
        sem.from_date = request.POST['from']
        sem.to_date = request.POST['to']
        sem.save()
        return redirect('semester')
    else:
        course = Course.objects.all()
        semester = Semester.objects.all()
        academic_year = AcademicYear.objects.all()
        semester_to_edit = Semester.objects.get(id=pk)
        return render(request,'semester.html',{'semesters':semester,'courses':course, 'academic_years':academic_year, 'semester_to_edit':semester_to_edit})

def semester_delete(request,pk):
    semester = Semester.objects.get(id=pk)
    semester.delete()
    return redirect('semester')


def academicyear(request):
    if request.method=='POST':     
        acyr = AcademicYear()
        acyr.from_year = request.POST['from_date']
        acyr.to_year = request.POST['to_date']
        acyr.name = request.POST['from_date'] + ' - ' + request.POST['to_date']
        acyr.save()
        academic_year = AcademicYear.objects.all()
        return render(request,'academicyear.html',{'academic_years':academic_year})
    else:
        academic_year = AcademicYear.objects.all()
        return render(request,'academicyear.html',{'academic_years':academic_year})

def academicyear_edit(request,pk):
    if request.method=='POST': 
        acyr = AcademicYear.objects.get(id=pk)
        acyr.from_year = request.POST['from_date']
        acyr.to_year = request.POST['to_date']
        acyr.name = request.POST['from_date'] + ' - ' + request.POST['to_date']
        acyr.save()
        return redirect('academicyear')
    else:
        academic_year = AcademicYear.objects.all()
        academic_year_to_edit = Semester.objects.get(id=pk)
        return render(request,'academicyear.html',{'academic_years':academic_year, 'academic_year_to_edit':academic_year_to_edit})

def academicyear_delete(request,pk):
    acyr = AcademicYear.objects.get(id=pk)
    acyr.delete()
    return redirect('academicyear')


def drop(request):
    course = Course.objects.all()
    semester = Semester.objects.all()
    return render(request,'drop.html',{'courses':course, 'semesters':semester})