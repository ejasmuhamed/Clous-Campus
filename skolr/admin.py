from django.contrib import admin
from .models import *

admin.site.register(AcademicYear)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Teacher)