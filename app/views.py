# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.aggregates import Count
from django.db.models.fields import IntegerField
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django import template
from django.urls import reverse

from rest_framework.response import Response
from rest_framework import generics
from .models import Pengguna, Pertanyaan, Jawaban, TingkatDepresi, HasilDeteksi, Penanganan, HistoryPertanyaanJawaban, Artikel
from .serializers import PenggunaSerializer, PertanyaanSerializer, JawabanSerializer, TingkatDepresiSerializer, HasilDeteksiSerializer, PenangananSerializer, HistoryPertanyaanJawabanSerializer, ArtikelSerializer
from .forms import *

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from rest_framework.decorators import api_view

from cloudinary.forms import cl_init_js_callbacks
from django.db.models import Q, query
import datetime
from django.db.models import Count
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler



# from django.shortcuts import render, redirect
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# from django.conf.urls.static import static
# import os
# # import tensorflow as tf
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# import json
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import MinMaxScaler
# import base64
# from io import BytesIO
# from sklearn import metrics
# from sklearn.metrics import confusion_matrix
# from sklearn.metrics import classification_report



# CLUSTERING

# @login_required(login_url="/login/")
# def clustering_data(request):
#     obj = HasilDeteksi.objects.filter(
#         ~Q(tingkatdepresi_id = 1)
#     ).values('pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan', 'tingkatdepresi_id__nama_depresi').annotate(obj=Count('tingkatdepresi_id')).order_by('pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan')
#     query_df = pd.DataFrame(obj)
#     query_df['initial'] = range(1, len(query_df) + 1)

#     selected_df = query_df[['obj']]
#     inisial_df = query_df[['initial']]

#     # change to array
#     x_array = np.array(inisial_df)

#     scaler = MinMaxScaler()
#     x_scaled = scaler.fit_transforms(x_array)
#     selected_df['initial'] = pd.DataFrame(np.array(x_scaled))

#     kmeans = KMeans(n_clusters=get_best_cluster, random_state=0).fit(selected_df)
#     query_df['kluster'] = kmeans.labels_







# @login_required(login_url="/login/")
# def clustering_data(request):
#     Pengguna.find_age()
#     born = Pengguna.objects.values('ttl')
#     makelist = list()
#     now = datetime.today().date()
#     age = now - born
#     obj = HasilDeteksi.objects.filter(
#         ~Q(tingkatdepresi_id = 1)
#     ).values('pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan', 'tingkatdepresi_id__nama_depresi').annotate(tingkatdepresi=Count('tingkatdepresi_id')).order_by('pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan')
#     # print(obj)
#     context = {
#         "object_list" : obj
#     }

#     template = "coba.html"    
#     return render(request, template, context)
# #     form = PertanyaanModelForm(request.POST or None)
# #     if form.is_valid():
# #         obj = form.save(commit=False)
# #         obj.save()
# #         return HttpResponseRedirect(reverse('app:list-pertanyaan'))
# HasilDeteksi.objects.filter(~Q(createdAt = )).values('pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan').annotate(tingkatdepresi=Count('tingkatdepresi_id'))

# .order_by('-createdAt').first()
# HasilDeteksi.objects.values('pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan').order_by('-createdAt').first()
# .annotate(tingkatdepresi=Count('tingkatdepresi_id')).order_by('pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan', '-createdAt').first()
# HasilDeteksi.objects(~Q(tingkatdepresi_id = 1)).values('pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan', 'tingkatdepresi_id__nama_depresi').annotate(tingkatdepresi=Count('tingkatdepresi_id')).order_by('pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan')
# obj = HasilDeteksi.objects.filter(~Q(tingkatdepresi_id = 1)).values(datetime.date.today() - 'pengguna_id__ttl', 'pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan').order_by('pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan')
# datetime.date.today() - self.date_of_birth
# HasilDeteksi.objects.filter(~Q(tingkatdepresi_id = 1)).values(date.today() - datetime.strptime('pengguna_id__ttl', '%Y-%m-%dT%H:%M:%S.%fZ'), 'pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan').order_by('pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan')
# HasilDeteksi.objects.filter(~Q(tingkatdepresi_id = 1)).values(int(date.today() - 'pengguna_id__ttl')), 'pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan').order_by('pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan')
# int((datetime.now().date() - self.birth_date).days / 365.25)
# HasilDeteksi.objects.filter(~Q(tingkatdepresi_id = 1)).values(datetime.today().strftime('%Y-%m-%d') - datetime.strptime('pengguna_id__ttl', '%Y-%m-%d').date(), 'pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan').order_by('pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan')
# pd.to_datetime('today').strftime('%Y-%m-%d')
# HasilDeteksi.objects.filter(~Q(tingkatdepresi_id = 1)).values(pd.to_datetime('today').strftime('%Y-%m-%d') - datetime.strptime('pengguna_id__ttl', '%b %d %Y').strftime('%y-%m-%d'), 'pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan').order_by('pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan')
# HasilDeteksi.objects.filter(~Q(tingkatdepresi_id = 1)).values(datetime.strptime('pengguna_id__ttl', '%Y-%m-%d').date()) 
# HasilDeteksi.objects.filter(~Q(tingkatdepresi_id = 1)).values('pengguna_id__ttl') 
# HasilDeteksi.objects.filter(~Q(tingkatdepresi_id = 1)).values(relativedelta(date.today(), 'pengguna_id__ttl')) 
# %a %b %d %H:%M:%S %Y
# HasilDeteksi.objects.filter(~Q(tingkatdepresi_id = 1)).values('pengguna_id__ttl') 
# list(Pengguna.objects.extra(select={'date':"to_char(ttl, 'YYYY-MM-DD')".format(IntegerField)}).values_list('date', flat='true'))
# list(Pengguna.objects.extra(select={'date':"to_char(ttl, 'YYYY')"}).values_list('date', flat='true'))
# HasilDeteksi.objects.filter(~Q('tingkatdepresi_id__' = 'nama_depresi')).values('pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan').annotate(tingkatdepresi=Count('tingkatdepresi_id')).order_by('pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan')



# LOGIN

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))





# CRUD API PENGGUNA

@api_view(['GET'])
def apiOverviewPengguna(request):
    api_urls={
        'List': 'pengguna-list',
        'Detail View': 'pengguna-detail/<int:id>/',
        'Create': 'pengguna-create',
        'Update View': 'pengguna-update/<int:id>/',
        'Delete View': 'pengguna-delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAllPengguna(request):
    pengguna = Pengguna.objects.all()
    serializer = PenggunaSerializer(pengguna, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewPengguna(request, pk):
    pengguna = Pengguna.objects.get(id=pk)
    serializer = PenggunaSerializer(pengguna, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def viewEmailPengguna(request, email):
    pengguna = Pengguna.objects.get(email=email)
    serializer = PenggunaSerializer(pengguna, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createPengguna(request):
    serializer = PenggunaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updatePengguna(request, pk):
    pengguna = Pengguna.objects.get(id=pk)
    serializer = PenggunaSerializer(instance=pengguna, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deletePengguna(request, pk):
    pengguna = Pengguna.objects.get(id=pk)
    pengguna.delete()  
    return Response('Items delete successfuly')

# CRUD UI PENGGUNA

@api_view(['GET'])
def overviewPengguna(request):
    api_urls={
        'List': 'app/pengguna',
        'Detail View': 'app/pengguna/detail/<int:id>/',
        # 'Create': 'pengguna/tambah/',
        # 'Update View': 'pengguna/edit/<int:id>/',
        # 'Delete View': 'pengguna/hapus/<int:id>/',
    }
    return Response(api_urls)

@login_required(login_url="/login/")
def delete_view_pengguna(request , id=None):
    obj = get_object_or_404(Pengguna, id=id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Items delete successfuly")
        return HttpResponseRedirect(reverse('app:list-pengguna'))

    context = {
        "object": obj
    }

    template = "pengguna/delete_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def update_view_pengguna(request, id=None):
    obj = get_object_or_404(Pengguna, id=id)
    form = PenggunaModelForm(request.POST or None, instance=obj)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        #print(obj.title)
        obj.save()
        messages.success(request, "Items updated successfuly")
        return HttpResponseRedirect(reverse('app:detail-pengguna', kwargs={'id':'{num}'.format(num=obj.id)}))
        # reverse('app:edit-pengguna', kwargs={'id':'{num}'.format(num=obj.id)})
    
    template = "pengguna/update_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def create_view_pengguna(request):
    form = PenggunaModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(reverse('app:list-pengguna'))
    context = {
        "form": form
    }
        
    template = "pengguna/create_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def detail_view_pengguna(request, id=None):
    print(id)
    qs = get_object_or_404(Pengguna, id=id)
    print(qs)
    context = {
        "object" : qs
    }

    template = "pengguna/detail_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def list_view_pengguna(request):
    query = request.GET.get("query", None)
    obj = Pengguna.objects.all()
    if query is not None:
        obj = obj.filter(title__icontains=query)
    
    context = {
        "object_list" : obj
    }

    template = "pengguna/list_view.html"    
    return render(request, template, context)





# CRUD API PERTANYAAN

@api_view(['GET'])
def apiOverviewPertanyaan(request):
    api_urls={
        'List': 'pertanyaan-list',
        'Detail View': 'pertanyaan-detail/<int:id>/',
        'Create': 'pertanyaan-create',
        'Update View': 'pertanyaan-update/<int:id>/',
        'Delete View': 'pertanyaan-delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAllPertanyaan(request):
    pertanyaan = Pertanyaan.objects.all()
    serializer = PertanyaanSerializer(pertanyaan, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewPertanyaan(request, pk):
    pertanyaan = Pertanyaan.objects.get(id=pk)
    serializer = PertanyaanSerializer(pertanyaan, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createPertanyaan(request):
    serializer = PertanyaanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updatePertanyaan(request, pk):
    pertanyaan = Pertanyaan.objects.get(id=pk)
    serializer = PertanyaanSerializer(instance=pertanyaan, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deletePertanyaan(request, pk):
    pertanyaan = Pertanyaan.objects.get(id=pk)
    pertanyaan.delete()  
    return Response('Items delete successfuly')

# CRUD UI PERTANYAAN

@api_view(['GET'])
def overviewPertanyaan(request):
    api_urls={
        'List': 'layanan/kuesioner/pertanyaan/',
        'Detail View': 'layanan/kuesioner/pertanyaan/detail/<int:id>/',
        'Create': 'layanan/kuesioner/pertanyaan/tambah/',
        'Update View': 'layanan/kuesioner/pertanyaan/edit/<int:id>/',
        'Delete View': 'layanan/kuesioner/pertanyaan/hapus/<int:id>/',
    }
    return Response(api_urls)

@login_required(login_url="/login/")
def delete_view_pertanyaan(request , id=None):
    obj = get_object_or_404(Pertanyaan, id=id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Items delete successfuly")
        return HttpResponseRedirect(reverse('app:list-pertanyaan'))

    context = {
        "object": obj
    }

    template = "kuesioner/pertanyaan/delete_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def update_view_pertanyaan(request, id=None):
    obj = get_object_or_404(Pertanyaan, id=id)
    form = PertanyaanModelForm(request.POST or None, instance=obj)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        #print(obj.title)
        obj.save()
        messages.success(request, "Items updated successfuly")
        return HttpResponseRedirect(reverse('app:detail-pertanyaan', kwargs={'id':'{num}'.format(num=obj.id)}))
        # reverse('app:edit-pertanyaan', kwargs={'id':'{num}'.format(num=obj.id)})
    
    template = "kuesioner/pertanyaan/update_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def create_view_pertanyaan(request):
    form = PertanyaanModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(reverse('app:list-pertanyaan'))
    context = {
        "form": form
    }
        
    template = "kuesioner/pertanyaan/create_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def detail_view_pertanyaan(request, id=None):
    print(id)
    qs = get_object_or_404(Pertanyaan, id=id)
    print(qs)
    context = {
        "object" : qs
    }

    template = "kuesioner/pertanyaan/detail_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def list_view_pertanyaan(request):
    query = request.GET.get("query", None)
    obj = Pertanyaan.objects.all()
    if query is not None:
        obj = obj.filter(title__icontains=query)
    
    context = {
        "object_list" : obj
    }

    template = "kuesioner/pertanyaan/list_view.html"    
    return render(request, template, context)





# CRUD API JAWABAN

@api_view(['GET'])
def apiOverviewJawaban(request):
    api_urls={
        'List': 'jawaban-list',
        'Detail View': 'jawaban-detail/<int:id>/',
        'Create': 'jawaban-create',
        'Update View': 'jawaban-update/<int:id>/',
        'Delete View': 'jawaban-delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAllJawaban(request):
    jawaban = Jawaban.objects.all()
    serializer = JawabanSerializer(jawaban, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewJawaban(request, pk):
    jawaban = Jawaban.objects.get(id=pk)
    serializer = JawabanSerializer(jawaban, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createJawaban(request):
    serializer = JawabanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateJawaban(request, pk):
    jawaban = Jawaban.objects.get(id=pk)
    serializer = JawabanSerializer(instance=jawaban, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deleteJawaban(request, pk):
    jawaban = Jawaban.objects.get(id=pk)
    jawaban.delete()  
    return Response('Items delete successfuly')

# CRUD UI JAWABAN

@api_view(['GET'])
def overviewJawaban(request):
    api_urls={
        'List': 'layanan/kuesioner/jawaban/',
        'Detail View': 'layanan/kuesioner/jawaban/detail/<int:id>/',
        'Create': 'layanan/kuesioner/jawaban/tambah/',
        'Update View': 'layanan/kuesioner/jawaban/edit/<int:id>/',
        'Delete View': 'layanan/kuesioner/jawaban/hapus/<int:id>/',
    }
    return Response(api_urls)

@login_required(login_url="/login/")
def delete_view_jawaban(request , id=None):
    obj = get_object_or_404(Jawaban, id=id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Items delete successfuly")
        return HttpResponseRedirect(reverse('app:list-jawaban'))

    context = {
        "object": obj
    }

    template = "kuesioner/jawaban/delete_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def update_view_jawaban(request, id=None):
    obj = get_object_or_404(Jawaban, id=id)
    form = JawabanModelForm(request.POST or None, instance=obj)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        #print(obj.title)
        obj.save()
        messages.success(request, "Items updated successfuly")
        return HttpResponseRedirect(reverse('app:detail-jawaban', kwargs={'id':'{num}'.format(num=obj.id)}))
        # reverse('app:edit-jawaban', kwargs={'id':'{num}'.format(num=obj.id)})
    
    template = "kuesioner/jawaban/update_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def create_view_jawaban(request):
    form = JawabanModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(reverse('app:list-jawaban'))
    context = {
        "form": form
    }
        
    template = "kuesioner/jawaban/create_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def detail_view_jawaban(request, id=None):
    print(id)
    qs = get_object_or_404(Jawaban, id=id)
    print(qs)
    context = {
        "object" : qs
    }

    template = "kuesioner/jawaban/detail_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def list_view_jawaban(request):
    query = request.GET.get("query", None)
    obj = Jawaban.objects.all()
    if query is not None:
        obj = obj.filter(title__icontains=query)
    
    context = {
        "object_list" : obj
    }

    template = "kuesioner/jawaban/list_view.html"    
    return render(request, template, context)





# CRUD API TINGKAT DEPRESI

@api_view(['GET'])
def apiOverviewTingkatDepresi(request):
    api_urls={
        'List': 'tingkatdepresi-list',
        'Detail View': 'tingkatdepresi-detail/<int:id>/',
        'Create': 'tingkatdepresi-create',
        'Update View': 'tingkatdepresi-update/<int:id>/',
        'Delete View': 'tingkatdepresi-delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAllTingkatDepresi(request):
    tingkatdepresi = TingkatDepresi.objects.all()
    serializer = TingkatDepresiSerializer(tingkatdepresi, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewTingkatDepresi(request, pk):
    tingkatdepresi = TingkatDepresi.objects.get(id=pk)
    serializer = TingkatDepresiSerializer(tingkatdepresi, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createTingkatDepresi(request):
    serializer = TingkatDepresiSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateTingkatDepresi(request, pk):
    tingkatdepresi = TingkatDepresi.objects.get(id=pk)
    serializer = TingkatDepresiSerializer(instance=tingkatdepresi, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deleteTingkatDepresi(request, pk):
    tingkatdepresi = TingkatDepresi.objects.get(id=pk)
    tingkatdepresi.delete()  
    return Response('Items delete successfuly')





# CRUD API HASIL DETEKSI

@api_view(['GET'])
def apiOverviewHasilDeteksi(request):
    api_urls={
        'List': 'hasildepresi-list',
        'Detail View': 'hasildeteksi-detail/<int:id>/',
        'Create': 'hasildeteksi-create',
        'Update View': 'hasildeteksi-update/<int:id>/',
        'Delete View': 'hasildeteksi-delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAllHasilDeteksi(request):
    hasildeteksi = HasilDeteksi.objects.all()
    serializer = HasilDeteksiSerializer(hasildeteksi, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewHasilDeteksi(request, pk):
    hasildeteksi = HasilDeteksi.objects.get(id=pk)
    serializer = HasilDeteksiSerializer(hasildeteksi, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def viewIdPenggunaHasilDeteksi(request, pengguna_id):
    hasildeteksi = HasilDeteksi.objects.all().filter(pengguna_id=pengguna_id)
    serializer = HasilDeteksiSerializer(hasildeteksi, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewRecentIdPenggunaHasilDeteksi(request, pengguna_id):
    hasildeteksi = HasilDeteksi.objects.filter(pengguna_id=pengguna_id).order_by('-createdAt').first()
    serializer = HasilDeteksiSerializer(hasildeteksi, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createHasilDeteksi(request):
    serializer = HasilDeteksiSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateHasilDeteksi(request, pk):
    hasildeteksi = HasilDeteksi.objects.get(id=pk)
    serializer = HasilDeteksiSerializer(instance=hasildeteksi, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deleteHasilDeteksi(request, pk):
    hasildeteksi = HasilDeteksi.objects.get(id=pk)
    hasildeteksi.delete()  
    return Response('Items delete successfuly')





# CRUD API PENANGANAN

@api_view(['GET'])
def apiOverviewPenanganan(request):
    api_urls={
        'List': 'penanganan-list',
        'Detail View': 'penanganan-detail/<int:id>/',
        'Create': 'penanganan-create',
        'Update View': 'penanganan-update/<int:id>/',
        'Delete View': 'penanganan-delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAllPenanganan(request):
    penanganan = Penanganan.objects.all()
    serializer = PenangananSerializer(penanganan, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewPenanganan(request, pk):
    penanganan = Penanganan.objects.get(id=pk)
    serializer = PenangananSerializer(penanganan, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def viewIdTingkatDepresiPenanganan(request, tingkatdepresi_id):
    penanganan = Penanganan.objects.get(tingkatdepresi_id=tingkatdepresi_id)
    serializer = PenangananSerializer(penanganan, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createPenanganan(request):
    serializer = PenangananSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updatePenanganan(request, pk):
    penanganan = Penanganan.objects.get(id=pk)
    serializer = PenangananSerializer(instance=penanganan, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deletePenanganan(request, pk):
    penanganan = Penanganan.objects.get(id=pk)
    penanganan.delete()  
    return Response('Items delete successfuly')

# CRUD UI PENANGANAN

@api_view(['GET'])
def overviewPenanganan(request):
    api_urls={
        'List': 'layanan/penanganan/',
        'Detail View': 'layanan/penanganan/detail/<int:id>/',
        'Create': 'layanan/penanganan/tambah/',
        'Update View': 'layanan/penanganan/edit/<int:id>/',
        'Delete View': 'layanan/penanganan/hapus/<int:id>/',
    }
    return Response(api_urls)

@login_required(login_url="/login/")
def delete_view_penanganan(request , id=None):
    obj = get_object_or_404(Penanganan, id=id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Items delete successfuly")
        return HttpResponseRedirect(reverse('app:list-penanganan'))

    context = {
        "object": obj
    }

    template = "penanganan/delete_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def update_view_penanganan(request, id=None):
    obj = get_object_or_404(Penanganan, id=id)
    form = PenangananModelForm(request.POST or None, request.FILES or None, instance=obj)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        #print(obj.title)
        obj.save()
        messages.success(request, "Items updated successfuly")
        return HttpResponseRedirect(reverse('app:detail-penanganan', kwargs={'id':'{num}'.format(num=obj.id)}))
        # reverse('app:edit-penanganan', kwargs={'id':'{num}'.format(num=obj.id)})
    
    template = "penanganan/update_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def create_view_penanganan(request):
    form = PenangananModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(reverse('app:list-penanganan'))
    context = {
        "form": form
    }
        
    template = "penanganan/create_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def detail_view_penanganan(request, id=None):
    print(id)
    qs = get_object_or_404(Penanganan, id=id)
    print(qs)
    context = {
        "object" : qs
    }

    template = "penanganan/detail_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def list_view_penanganan(request):
    query = request.GET.get("query", None)
    obj = Penanganan.objects.all()
    if query is not None:
        obj = obj.filter(title__icontains=query)
    
    context = {
        "object_list" : obj
    }

    template = "penanganan/list_view.html"    
    return render(request, template, context)




# CRUD API HISTORY PERTANYAAN JAWABAN

@api_view(['GET'])
def apiOverviewHistoryPertanyaanJawaban(request):
    api_urls={
        'List': 'historypertanyaanjawaban-list',
        'Detail View': 'historypertanyaanjawaban-detail/<int:id>/',
        'Create': 'historypertanyaanjawaban-create',
        'Update View': 'historypertanyaanjawaban-update/<int:id>/',
        'Delete View': 'historypertanyaanjawaban-delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAllHistoryPertanyaanJawaban(request):
    historypertanyaanjawaban = HistoryPertanyaanJawaban.objects.all()
    serializer = HistoryPertanyaanJawaban(historypertanyaanjawaban, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewHistoryPertanyaanJawaban(request, pk):
    historypertanyaanjawaban = HistoryPertanyaanJawaban.objects.get(id=pk)
    serializer = HistoryPertanyaanJawabanSerializer(historypertanyaanjawaban, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createHistoryPertanyaanJawaban(request):
    serializer = HistoryPertanyaanJawabanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateHistoryPertanyaanJawaban(request, pk):
    historypertanyaanjawaban = HistoryPertanyaanJawaban.objects.get(id=pk)
    serializer = HistoryPertanyaanJawabanSerializer(instance=historypertanyaanjawaban, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deleteHistoryPertanyaanJawaban(request, pk):
    historypertanyaanjawaban = HistoryPertanyaanJawaban.objects.get(id=pk)
    historypertanyaanjawaban.delete()  
    return Response('Items delete successfuly')





# CRUD API ARTIKEL

@api_view(['GET'])
def apiOverviewArtikel(request):
    api_urls={
        'List': 'artikel-list',
        'Detail View': 'artikel-detail/<int:id>/',
        'Create': 'artikel-create',
        'Update View': 'artikel-update/<int:id>/',
        'Delete View': 'artikel-delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAllArtikel(request):
    artikel = Artikel.objects.all()
    serializer = ArtikelSerializer(artikel, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewArtikel(request, pk):
    artikel = Artikel.objects.get(id=pk)
    serializer = ArtikelSerializer(artikel, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createArtikel(request):
    serializer = ArtikelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateArtikel(request, pk):
    artikel = Artikel.objects.get(id=pk)
    serializer = ArtikelSerializer(instance=artikel, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deleteArtikel(request, pk):
    artikel = Artikel.objects.get(id=pk)
    artikel.delete()  
    return Response('Items delete successfuly')

# CRUD UI ARTIKEL

@api_view(['GET'])
def overviewArtikel(request):
    api_urls={
        'List': 'layanan/artikel/',
        'Detail View': 'layanan/artikel/detail/<int:id>/',
        'Create': 'layanan/artikel/tambah/',
        'Update View': 'layanan/artikel/edit/<int:id>/',
        'Delete View': 'layanan/artikel/hapus/<int:id>/',
    }
    return Response(api_urls)

@login_required(login_url="/login/")
def delete_view_artikel(request , id=None):
    obj = get_object_or_404(Artikel, id=id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Items delete successfuly")
        return HttpResponseRedirect(reverse('app:list-artikel'))

    context = {
        "object": obj
    }

    template = "artikel/delete_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def update_view_artikel(request, id=None):
    obj = get_object_or_404(Artikel, id=id)
    form = ArtikelModelForm(request.POST or None, request.FILES or None, instance=obj)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        #print(obj.title)
        obj.save()
        messages.success(request, "Items updated successfuly")
        return HttpResponseRedirect(reverse('app:detail-artikel', kwargs={'id':'{num}'.format(num=obj.id)}))
        # reverse('app:edit-artikel', kwargs={'id':'{num}'.format(num=obj.id)})
    
    template = "artikel/update_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def create_view_artikel(request):
    form = ArtikelModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(reverse('app:list-artikel'))
    context = {
        "form": form
    }
        
    template = "artikel/create_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def detail_view_artikel(request, id=None):
    print(id)
    qs = get_object_or_404(Artikel, id=id)
    print(qs)
    context = {
        "object" : qs
    }

    template = "artikel/detail_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def list_view_artikel(request):
    query = request.GET.get("query", None)
    obj = Artikel.objects.all()
    if query is not None:
        obj = obj.filter(title__icontains=query)
    
    context = {
        "object_list" : obj
    }

    template = "artikel/list_view.html"    
    return render(request, template, context)





