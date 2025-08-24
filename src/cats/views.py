from django.shortcuts import render
from .models import Cat

# Create your views here.
def index(request):
    cats = Cat.objects.prefetch_related("results").all()
    context = {
        'cats':cats
    }
    return render(request, "cats/index.html", context)