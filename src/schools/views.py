from django.shortcuts import render
from .models import School

# Create your views here.
def index(request):
    schools = School.objects.prefetch_related("classes","students","teachers","clubs","courses", "exams").all()
    page_title = "Schools"
    context = {
        'page_title': page_title,
        'schools':schools
    }
    return render(request, "sync_apps/schools/index.html", context)