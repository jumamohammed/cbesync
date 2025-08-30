from django.shortcuts import render
from .models import Communication, CommunicationGroup, CommunicationGroupMember
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    page_title = "Comms"
    if request.user.is_authenticated:
        communications = Communication.objects.all()
        communication_groups = CommunicationGroup.objects.prefetch_related("members").all()
        communication_group_members = CommunicationGroupMember.objects.all()
        context = {
            'page_title': page_title
        }
    else:
        context = {
            'page_title': page_title
        }
    return render(request, "sync_apps/comms/index.html", context)