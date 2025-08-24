from django.shortcuts import render
from .models import Teacher

# Create your views here.
def index(request):
    teachers = Teacher.objects.prefetch_related("supervised_cats", "supervised_exams", "graded_results","classes_t", "patron_clubs", "supervised_projects", "subjects").all()
    context = {
        'teachers':teachers
    }
    return render(request, "teachers/index.html", context)