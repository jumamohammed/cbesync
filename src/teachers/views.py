from django.shortcuts import render
from .models import Teacher
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    page_title = "Teachers"
    if request.user.is_authenticated:
        teachers = Teacher.objects.prefetch_related("supervised_cats", "supervised_exams", "graded_results","classes_t", "patron_clubs", "supervised_projects", "subjects").all()
        context = {
            'page_title': page_title,
            'teachers':teachers
        }
    else:
        context = {
            'page_title': page_title
        }
    return render(request, "sync_apps/teachers/index.html", context)