from django.shortcuts import render
from .models import Club

# Create your views here.
def index(request):
    clubs = Club.objects.prefetch_related("students").all()
    page_title = "Clubs"
    context = {
        'page_title': page_title
    }
    return render(request, "sync_apps/clubs/index.html", context)