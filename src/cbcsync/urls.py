"""
URL configuration for cbcsync project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import views
from django.urls import path, include
from auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #logged out user access
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('services/',views.services, name="services"),
    #process to login/register users
    path('login/', auth_views.login_view, name="login"),
    path('register/', auth_views.register_view, name="register"),
    path('accounts/', include('allauth.urls')), #login user and logout

    #logged in users apps
    path('account/', include('accounts.urls')),
    path('assessment/', include('assessments.urls')),
    path('school/', include('schools.urls')),
    path('course/', include('courses.urls')),
    path('club/', include('clubs.urls')),
    path('material/', include('materials.urls')),
    path('class/', include('classes.urls')),
    path('teacher/', include('teachers.urls')),
    path('student/', include('students.urls')),
    path('parent/', include('parents.urls')),
    path('comm/', include('comms.urls')),
    path('subject/', include('subjects.urls')),
    path('result/', include('results.urls')),
    path('exam/', include('exams.urls')),
    path('cat/', include('cats.urls')),
    path('project/', include('projects.urls')),
]

