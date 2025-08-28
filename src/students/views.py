from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    page_title = "Students"
    if request.user.is_authenticated:
        students = Student.objects.prefetch_related("exams", "cats", "projects", "results", "subjects").all()
        context = {
            'page_title': page_title,
            'students':students
        }
    else:
        context = {
            'page_title': page_title
        }
    return render(request, "sync_apps/students/index.html", context)