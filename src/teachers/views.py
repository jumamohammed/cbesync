from django.shortcuts import render
from .models import Teacher

# Create your views here.
def index(request):
    teachers = Teacher.objects.prefetch_related("supervised_cats", "supervised_exams", "graded_results","classes_t", "patron_clubs", "supervised_projects", "subjects").all()
    page_title = "Teachers"
    context = {
        'page_title': page_title
    }
    return render(request, "sync_apps/teachers/index.html", context)