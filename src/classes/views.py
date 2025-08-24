from django.shortcuts import render
from .models import SchoolClass

# Create your views here.
def index(request):
    classes = SchoolClass.objects.prefetch_related("students", "cats", "exams", "projects", "results", "subjects").all()
    page_title = "Classes"
    context = {
        'page_title': page_title
    }
    return render(request, "sync_apps/classes/index.html", context)