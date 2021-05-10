# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse,JsonResponse
# from .models import Pertanyaan
# from rest_framework import compat
# from django.views import View
# from rest_framework.response import Response 
# from rest_framework import status 
# from rest_framework.views import APIView
# from django.db.models import Q
# import json
# from django.contrib import messages
# from .forms import PertanyaanModelForm

# from .serializers import CreateSerializer
# from django.http import *
# from rest_framework.decorators import api_view

# # API

# @api_view(['GET'])
# def apiOverviewPertanyaan(request):
#     api_urls={
#         'List': 'list',
#         'Detail View': 'detail/<int:id>/',
#         'Create': 'create',
#         'Update View': 'update/<int:id>/',
#         'Delete View': 'delete/<int:id>/',
#     }
#     return Response(api_urls)

# @api_view(['GET'])
# def showAll(request):
#     pertanyaan = Pertanyaan.objects.all()
#     serializer = CreateSerializer(pertanyaan, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def view(request, pk):
#     pertanyaan = Pertanyaan.objects.get(id=pk)
#     serializer = CreateSerializer(pertanyaan, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create(request):
#     serializer = CreateSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['POST'])
# def update(request, pk):
#     pertanyaan = Pertanyaan.objects.get(id=pk)
#     serializer = CreateSerializer(instance=pertanyaan, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['GET'])
# def delete(request, pk):
#     pertanyaan = Pertanyaan.objects.get(id=pk)
#     pertanyaan.delete()  
#     return Response('Items delete successfuly')


# # UI

# @login_required(login_url="/login/")
# def delete_view(request , id=None):
#     obj = get_object_or_404(Pertanyaan, id=id)
#     if request.method == 'POST':
#         obj.delete()
#         messages.success(request, "Items delete successfuly")
#         return HttpResponseRedirect("/layanan/kuesioner/pertanyaan/list/")

#     context = {
#         "object": obj
#     }

#     template = "kuesioner/delete_view.html"
#     return render(request, template, context)



# @login_required(login_url="/login/")
# def update_view(request, id=None):
#     obj = get_object_or_404(Pertanyaan, id=id)
#     form = PertanyaanModelForm(request.POST or None, instance=obj)
#     context = {
#         "form": form
#     }
#     if form.is_valid():
#         obj = form.save(commit=False)
#         #print(obj.title)
#         obj.save()
#         messages.success(request, "Items updated successfuly")
#         return HttpResponseRedirect("/layanan/kuesioner/pertanyaan/detail/{num}".format(num=obj.id))
    
#     template = "kuesioner/update_view.html"
#     return render(request, template, context)

# @login_required(login_url="/login/")
# def create_view(request):
#     form = PertanyaanModelForm(request.POST or None)
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.save()
#         return HttpResponseRedirect("/layanan/kuesioner/pertanyaan/list/")
#     context = {
#         "form": form
#     }
        
#     template = "kuesioner/create_view.html"
#     return render(request, template, context)

# @login_required(login_url="/login/")
# def detail_view(request, id=None):
#     print(id)
#     qs = get_object_or_404(Pertanyaan, id=id)
#     print(qs)
#     context = {
#         "object" : qs
#     }

#     template = "kuesioner\detail_view.html"
#     return render(request, template, context)

# @login_required(login_url="/login/")
# def list_view(request):
#     query = request.GET.get("qury", None)
#     obj = Pertanyaan.objects.all()
#     if query is not None:
#         obj = obj.filter(title__icontains=query)
    
#     context = {
#         "object_list" : obj
#     }

#     template = "kuesioner\list_view.html"    
#     return render(request, template, context)