from django.db import models

class Department(models.Model):
    name = models.CharField(max_length = 100)
    code = models.CharField(max_length = 10)
    hod = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

class AcademicYear(models.Model):
    from_year = models.IntegerField()
    to_year = models.IntegerField()
    name = models.CharField(max_length = 20)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    staff_id = models.CharField(max_length = 10)
    name = models.CharField(max_length = 200)
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    typ = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Course(models.Model):
    c_id = models.CharField(max_length = 10)
    name = models.CharField(max_length = 150)
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    def __str__(self):
        return self.name

class Batch(models.Model):
    name = models.CharField(max_length = 10)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)

class Semester(models.Model):
    number = models.IntegerField()
    academic_year = models.ForeignKey(AcademicYear, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    course = models.ForeignKey(Course, on_delete = models.CASCADE) #course is called here, so no need of calling Course wherever Semester is called
    from_date = models.DateField()
    to_date = models.DateField()

class Subject(models.Model):
    semster = models.ForeignKey(Semester, on_delete = models.CASCADE) #Course in not called because it is called inside the class Semester
    name = models.CharField(max_length = 150)
    typ = models.CharField(max_length = 50)
    exam1 = models.BooleanField()
    exam2 = models.BooleanField()
    attendence = models.BooleanField()
    assignment = models.BooleanField()
    seminar = models.BooleanField(default = False)
    exam1_internal_max = models.IntegerField()
    exam2_internal_max = models.IntegerField()
    attendence_internal_max = models.IntegerField()
    assignment_internal_max = models.IntegerField()
    seminar_internal_max = models.IntegerField()

class Student(models.Model):
    roll_number = models.IntegerField()
    register_number = models.IntegerField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE) #Course in not called because it is called inside the class Semester
    batch = models.ForeignKey(Batch, on_delete = models.CASCADE)

class InternalMark(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE) #Semsester is already called inaside student, Course is called inside Semester, So no need of both Foreign Keys
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    exam1_internal = models.IntegerField()
    exam2_internal = models.IntegerField()
    attendence_internal = models.IntegerField()
    assignment_internal = models.IntegerField()
    seminar_internal = models.IntegerField()

