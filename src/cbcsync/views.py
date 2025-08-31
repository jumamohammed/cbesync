from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
                # import logging
                # from django.http import HttpResponse
                # import os
                # logger = logging.getLogger("accounts.views")

                # #fucntion to simplif ip capture
                # def ipread(request):
                #     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                #     ip = x_forwarded_for.split(',')[0].strip() if x_forwarded_for else request.META.get('REMOTE_ADDR', '')
                #     if request.user.is_authenticated:
                #         logger.info(f"Logged in user from IP: {ip}")
                #     else:
                #         logger.info(f"Unauthenticated user from IP: {ip}")    
# Create your views here.
@login_required
def home(request):
                # #home view logger
                # ipread(request)
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

def index(request):
                # #home view logger
                # ipread(request)
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