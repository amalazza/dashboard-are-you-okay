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

# @api_view(['GET'])
# def apiOverview(request):
#     api_urls={
#         'List': 'pertanyaan-list',
#     }
#     return Response(api_urls)

# @api_view(['GET'])
# def showAll(request):
#     query = Pertanyaan.objects.all()
#     serializer = CreateSerializer(query, many=True)
#     return Response(serializer.data)

class ApiView(APIView):
    def get(self, request):
        query = Pertanyaan.objects.all()
        serializer = CreateSerializer(query, many=True)
        return Response(serializer.data)