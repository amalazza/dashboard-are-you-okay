from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
from .models import Pertanyaan
from rest_framework import compat
from django.views import View
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.views import APIView
from django.db.models import Q
import json
from django.contrib import messages
from .forms import PertanyaanModelForm

from .serializers import CreateSerializer
from django.http import *
from rest_framework.decorators import api_view

# class ApiView(APIView):
#     def get(self, request):
#         query = Pertanyaan.objects.all()
#         serializer = CreateSerializer(query, many=True)
#         return Response(serializer.data)

@api_view(['GET'])
def apiOverviewPertanyaan(request):
    api_urls={
        'List': 'list',
        'Detail View': 'detail/<int:id>/',
        'Create': 'create',
        'Update View': 'update/<int:id>/',
        'Delete View': 'delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAll(request):
    pertanyaan = Pertanyaan.objects.all()
    serializer = PertanyaanSerializer(pertanyaan, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def view(request, pk):
    pertanyaan = Pertanyaan.objects.get(id=pk)
    serializer = PertanyaanSerializer(pertanyaan, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = PertanyaanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def update(request, pk):
    pertanyaan = Pertanyaan.objects.get(id=pk)
    serializer = PertanyaanSerializer(instance=pertanyaan, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def delete(request, pk):
    pertanyaan = Pertanyaan.objects.get(id=pk)
    pertanyaan.delete()  
    return Response('Items delete successfuly')