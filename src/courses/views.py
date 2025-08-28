from django.shortcuts import render
from .models import Course

# Create your views here.
def index(request):
    page_title = "Courses"
    if request.user.is_authenticated:
        courses = Course.objects.all()
        context = {
            'page_title': page_title
        }
    else:
        context = {
            'page_title': page_title
        }
    return render(request, "sync_apps/courses/index.html", context)