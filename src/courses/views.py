from .models import Course
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
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