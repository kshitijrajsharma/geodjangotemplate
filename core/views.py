from django.shortcuts import render
from .models import location
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *

# Create your views here.
@api_view(['GET'])
def locationapi(request):
    
        data= location.objects.all()
        serializer= locationSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
