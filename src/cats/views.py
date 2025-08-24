from django.shortcuts import render
from .models import Cat

# Create your views here.
def index(request):
    cats = Cat.objects.prefetch_related("results").all()
    page_title = "Cats"
    context = {
        'page_title': page_title
    }
    return render(request, "sync_apps/cats/index.html", context)