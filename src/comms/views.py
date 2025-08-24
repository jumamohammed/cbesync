from django.shortcuts import render
from .models import Communication, CommunicationGroup, CommunicationGroupMember

# Create your views here.
def index(request):
    communications = Communication.objects.all()
    communication_groups = CommunicationGroup.objects.prefetch_related("members").all()
    communication_group_members = CommunicationGroupMember.objects.all()
    context = {
        'communications':communications,
        'communication_groups':communication_groups,
        'communication_group_members':communication_group_members
    }
    return render(request, "comms/index.html", context)