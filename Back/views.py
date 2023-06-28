from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.

class HomeViewset(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

class ContactViewset(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer


class AboutViewset(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class MembersViewset(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer