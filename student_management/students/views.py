from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student
from .forms import StudentForm

#  List Students (Read)
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

#  Create Student (Create)
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")  # ✅ Success message
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

#  Update Student (Update)
def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully!")  # ✅ Success message
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

#  Delete Student (Delete)
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Student record deleted!")  # ✅ Success message
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})
