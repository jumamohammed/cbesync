from .models import School
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required
def index(request):
    page_title = "Schools"

    if request.user.is_authenticated:
        schools = School.objects.prefetch_related("classes","students","teachers","clubs","courses", "exams").all()
        context = {
            'page_title': page_title,
            'schools':schools
        }
    else:
        context={
            'page_title': page_title
        }
    return render(request, "sync_apps/schools/index.html", context)