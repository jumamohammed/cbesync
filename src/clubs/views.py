from django.shortcuts import render
from .models import Club

# Create your views here.
def index(request):
    clubs = Club.objects.prefetch_related("students").all()
    context = {
        'clubs':clubs
    }
    return render(request, "clubs/index.html", context)