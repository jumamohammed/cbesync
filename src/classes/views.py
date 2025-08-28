from django.shortcuts import render
from .models import SchoolClass

# Create your views here.
def index(request):
    classes = SchoolClass.objects.prefetch_related("students", "cats", "exams", "projects", "results", "subjects").all()
    page_title = "Classes"
    if request.user.is_authenticated:
        context = {
            'page_title': page_title
        }
    else:
        context = {
            'page_title': page_title
        }
    return render(request, "sync_apps/classes/index.html", context)