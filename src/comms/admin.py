from django.contrib import admin
from .models import Communication, CommunicationGroup, CommunicationGroupMember

# Register your models here.
admin.site.register(Communication)
admin.site.register(CommunicationGroup)
admin.site.register(CommunicationGroupMember)