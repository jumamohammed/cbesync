from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import logging
from django.http import HttpResponse
import os
logger = logging.getLogger(__name__)



# Create your views here.
def home(request):
    # Log the file access
    logger.info(f"Connected user from IP: {request.META.get('REMOTE_ADDR')}")

    # Check if there's a stored redirect URL in the session
    redirect_url = request.session.pop('redirect_url', None)  # Pop to prevent it from being reused
    
    if redirect_url:
        return redirect(redirect_url)  # Redirect to the stored URL
    else:
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