from .models import Club
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    clubs = Club.objects.prefetch_related("students").all()
    page_title = "Clubs"
    if request.user.is_authenticated:
        context = {
            'page_title': page_title
        }
    else:
        context = {
            'page_title': page_title
        }
    return render(request, "sync_apps/clubs/index.html", context)