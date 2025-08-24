from django.shortcuts import render
from .models import Communication, CommunicationGroup, CommunicationGroupMember

# Create your views here.
def index(request):
    communications = Communication.objects.all()
    communication_groups = CommunicationGroup.objects.prefetch_related("members").all()
    communication_group_members = CommunicationGroupMember.objects.all()
    page_title = "Comms"
    context = {
        'page_title': page_title
    }
    return render(request, "sync_apps/comms/index.html", context)