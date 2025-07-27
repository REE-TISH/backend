from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def HomePageData(request):
    return Response({
        'User':'Reetish',
        'body':'hello everyone is this workng'
    })


