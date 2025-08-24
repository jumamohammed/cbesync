from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.prefetch_related("exams", "cats", "projects", "results", "subjects").all()
    page_title = "Students"
    context = {
        'page_title': page_title,
        'students':students
    }
    return render(request, "sync_apps/students/index.html", context)