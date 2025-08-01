from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
# Create your views here.

@api_view(['GET'])
def HomePageData(request):
    return Response({
        'avatar':'https://i.pinimg.com/736x/3e/ce/29/3ece2976d357f517d7da207b2bc0077e.jpg',
        'User':'Ashley',
        'body':'Play Resident evil requem'
    })

class CreateProfileView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
