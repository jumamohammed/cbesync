from django.shortcuts import render
from .models import Course

# Create your views here.
def index(request):
    courses = Course.objects.all()
    page_title = "Courses"
    context = {
        'page_title': page_title
    }
    return render(request, "sync_apps/courses/index.html", context)