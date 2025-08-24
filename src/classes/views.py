from django.shortcuts import render
from .models import SchoolClass

# Create your views here.
def index(request):
    classes = SchoolClass.objects.prefetch_related("students", "cats", "exams", "projects", "results", "subjects").all()
    return render(request, "classes/index.html", {})