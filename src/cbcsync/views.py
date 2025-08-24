from django.shortcuts import render

# Create your views here.
def index(request):
    page_title = "Home"
    context = {
        'page_title': page_title
    }
    return render(request, "root/index.html", context)

#about page views
def about(request):
    page_title = "About"
    context = {
        'page_title': page_title
    }
    return render(request, "root/about.html", context)
#services view
def services(request):
    page_title = "Services"
    context = {
        'page_title': page_title
    }
    return render(request, "root/services.html", context)
#contact view
def contact(request):
    page_title = "Contact"
    context = {
        'page_title': page_title
    }
    return render(request, "root/contact.html", context)