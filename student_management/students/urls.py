from django.urls import path
from .views import student_list, student_create, student_update, student_delete

urlpatterns = [
    path('', student_list, name='student_list'),
    path('add/', student_create, name='student_create'),
    path('edit/<int:id>/', student_update, name='student_update'),
    path('delete/<int:id>/', student_delete, name='student_delete'),
]
