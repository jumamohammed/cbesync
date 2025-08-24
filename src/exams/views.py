from django.shortcuts import render
from .models import Exam

# Create your views here.
def index(request):
    exams = Exam.objects.prefetch_related("results").all()
    context = {
        'exams':exams
    }
    return render(request, "exams/index.html", context)