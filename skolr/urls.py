from django.urls import path
from skolr import urls
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('department/', views.department, name='department'),
    path('department/edit/<int:pk>', views.department_edit, name='department_edit'),
    path('department/delete/<int:pk>', views.department_delete, name='department_delete'),
    path('course/', views.course, name='course'),
    path('course/edit/<int:pk>', views.course_edit, name='course_edit'),
    path('course/delete/<int:pk>', views.course_delete, name='course_delete'),
    path('semester/', views.semester, name='semester'),
    path('semester/edit/<int:pk>', views.semester_edit, name='semester_edit'),
    path('semester/delete/<int:pk>', views.semester_delete, name='semester_delete'),
    path('academic-year/', views.academicyear, name='academicyear'),
    path('academic-year/edit/<int:pk>', views.academicyear_edit, name='academicyear_edit'),
    path('academic-year/delete/<int:pk>', views.academicyear_delete, name='academicyear_delete'),

    path('drop', views.drop, name='drop'),
]
