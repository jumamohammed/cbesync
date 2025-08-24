from django.shortcuts import render
from .models import School

# Create your views here.
def index(request):
    schools = School.objects.prefetch_related("classes","students","teachers","clubs","courses", "exams").all()
    context = {
        'schools':schools,
    }
    return render(request, "schools/index.html", context)