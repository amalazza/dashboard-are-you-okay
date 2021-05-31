# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
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
from django.db.models import Q, query, Exists, F
import datetime
from django.db.models import Count
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import davies_bouldin_score
import seaborn as sns

from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale, StandardScaler
from numpy import random, float, array
import numpy as np
import seaborn as sns
from matplotlib import pylab
from pylab import *
from io import BytesIO
import base64

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger





# CLUSTERING DATA

@login_required(login_url="/login/")
def index(request):
    tidakdepresi = HasilDeteksi.objects.filter(~Q(tingkatdepresi_id = 2) & ~Q(tingkatdepresi_id = 3) & ~Q(tingkatdepresi_id = 4)).count()
    depresiringan = HasilDeteksi.objects.filter(~Q(tingkatdepresi_id = 1) & ~Q(tingkatdepresi_id = 3) & ~Q(tingkatdepresi_id = 4)).count()
    depresisedang = HasilDeteksi.objects.filter(~Q(tingkatdepresi_id = 1) & ~Q(tingkatdepresi_id = 2) & ~Q(tingkatdepresi_id = 4)).count()
    depresiberat = HasilDeteksi.objects.filter(~Q(tingkatdepresi_id = 1) & ~Q(tingkatdepresi_id = 2) & ~Q(tingkatdepresi_id = 3)).count()

    bar_depresi = HasilDeteksi.objects.values('tingkatdepresi_id__nama_depresi').annotate(bar_depresi=Count('tingkatdepresi_id'))
    query_df_bar = pd.DataFrame(bar_depresi)
    plt.bar(query_df_bar['tingkatdepresi_id__nama_depresi'], query_df_bar['bar_depresi']) 
    plt.xlabel('Jenis Depresi')
    plt.ylabel('Jumlah Depresi')
    plt.tight_layout()
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic1 = base64.b64encode(image_png)
    graphic1 = graphic1.decode('utf-8')
    pylab.close()

    plt.pie(query_df_bar['bar_depresi'],labels=query_df_bar['tingkatdepresi_id__nama_depresi'],autopct='%1.2f%%')
    plt.tight_layout()
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic2 = base64.b64encode(image_png)
    graphic2 = graphic2.decode('utf-8')
    pylab.close()


    # depresi = HasilDeteksi.objects.filter(
    #     ~Q(tingkatdepresi_id = 1)
    # ).values(
    #     'pengguna_id__umur', 'pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan', 'tingkatdepresi_id__nama_depresi').annotate(
    #         depresi=Count('tingkatdepresi_id')).order_by('pengguna_id__umur', 'pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan', 'tingkatdepresi_id__nama_depresi')
    depresi = HasilDeteksi.objects.values(
        'pengguna_id__umur', 'pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan', 'tingkatdepresi_id').annotate(
            depresi=Count('tingkatdepresi_id')).order_by('pengguna_id__umur', 'pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan', 'tingkatdepresi_id')
    query_df = pd.DataFrame(depresi)
    query_df['initial'] = range(1, len(query_df) + 1)

    selected_df = query_df[['tingkatdepresi_id']]
    inisial_df = query_df[['initial']]

    # change to array
    x_array = np.array(inisial_df)

    scaler = MinMaxScaler()
    x_scaled = scaler.fit_transform(x_array)
    selected_df['initial'] = pd.DataFrame(np.array(x_scaled))
    
    scoreDBI = [None] * 10
    for i in range(2, 10):
        kmeans_test = KMeans(n_clusters=i, random_state=0).fit(selected_df)
        DBI = davies_bouldin_score(selected_df, kmeans_test.labels_)
        scoreDBI[i] = DBI

    del scoreDBI[0:2]
    get_best_cluster = scoreDBI.index(min(scoreDBI)) + 2

    kmeans = KMeans(n_clusters=get_best_cluster, random_state=0).fit(selected_df)
    query_df['kluster'] = kmeans.labels_
    
    scatter_x = np.array(selected_df['initial'])
    scatter_y = np.array(selected_df['tingkatdepresi_id'])
    group = kmeans.labels_
    cdict = {0: 'pink', 1: 'blue', 2: 'orange', 3: 'green', 4: 'red', 5: 'purple', 6: 'brown', 7: 'gray', 8: 'olive', 9: 'cyan', 10: 'yellow', 11: 'steelblue', 12: 'palegreen', 13: 'indigo', 14: 'crimson', 15: 'sienna'}
    # centers = np.array(kmeans.cluster_centers_)

    fig, ax = plt.subplots()
    for g in np.unique(group):
        ix = np.where(group == g)
        # ax.scatter(centers[:, 0], centers[:, 0], marker="x", color='r')
        ax.scatter(scatter_x[ix], scatter_y[ix], c = cdict[g], label =g, s = 100)
    ax.legend()
    
    # plt.scatter(selected_df['initial'], selected_df['depresi'], 
    # c=[plt.cm.get_cmap("Spectral")(float(i) / (int(get_best_cluster)+1)) for i in kmeans.labels_])
    plt.xlabel('Inisialisasi: Umur, Jenis Kelamin, Status Pekerjaan')
    plt.ylabel('Jenis Depresi')
    plt.grid()
    
    plt.tight_layout()
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    pylab.close()

    # query_df.columns = ['Umur', 'Jenis Kelamin', 'Status Pekerjaan', 'Jenis Depresi', 'Jumlah Depresi', 'Initial', 'Cluster']
    query_df.drop('initial', inplace=True, axis=1)
    query_df.drop('depresi', inplace=True, axis=1)
    query_df.columns = ['Umur', 'Jenis Kelamin', 'Status Pekerjaan', 'Jenis Depresi', 'Cluster']

    context = {
        'title': "Applied K-Means",
        'k': get_best_cluster,
        'df': query_df.to_html(classes=["table-bordered", "table-responsive", "table-striped", "table-hover", "text-center"]),
        'graphic': graphic,
        'graphic1': graphic1,
        'graphic2': graphic2,
        'obj_tidakdepresi': tidakdepresi,
        'obj_depresiringan': depresiringan,
        'obj_depresisedang': depresisedang,
        'obj_depresiberat': depresiberat,
    }
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
    obj = HasilDeteksi.objects.filter(pengguna_id=id).order_by('-createdAt')
    page = request.GET.get('page', 1)
    paginator = Paginator(obj, 5)
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)

    print(qs)
    context = {
        "object" : qs,
        "object_list" : obj
    }

    template = "pengguna/detail_view.html"
    return render(request, template, context)

@login_required(login_url="/login/")
def list_view_pengguna(request):
    query = request.GET.get("query", None)
    obj = Pengguna.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(obj, 5)
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)
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
    page = request.GET.get('page', 1)
    paginator = Paginator(obj, 5)
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)

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
    page = request.GET.get('page', 1)
    paginator = Paginator(obj, 5)
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)

    if query is not None:
        obj = obj.filter(title__icontains=query)
    
    context = {
        "object_list" : obj
    }

    template = "artikel/list_view.html"    
    return render(request, template, context)





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
#     depresi = HasilDeteksi.objects.filter(
#         ~Q(tingkatdepresi_id = 1)
#     ).values('pengguna_id__umur', 'pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan', 'tingkatdepresi_id__nama_depresi').annotate(depresi=Count('tingkatdepresi_id')).order_by('pengguna_id__umur', 'pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan', 'tingkatdepresi_id__nama_depresi')
#     query_df = pd.DataFrame(depresi)
#     query_df['initial'] = range(1, len(query_df) + 1)

#     selected_df = query_df[['depresi']]
#     inisial_df = query_df[['initial']]

#     # change to array
#     x_array = np.array(inisial_df)

#     scaler = MinMaxScaler()
#     x_scaled = scaler.fit_transform(x_array)
#     selected_df['initial'] = pd.DataFrame(np.array(x_scaled))
#     # selected_df['initial'] = selected_df['initial'].reshape(-1, 1)
#     # sdi=pd.DataFrame(np.array(x_scaled))
#     # sdi=selected_df['initial2']
    
    
#     scoreDBI = [None] * 10
#     for i in range(2, 10):
#         kmeans_test = KMeans(n_clusters=i, random_state=0).fit(selected_df)
#         DBI = davies_bouldin_score(selected_df, kmeans_test.labels_)
#         scoreDBI[i] = DBI

#     del scoreDBI[0:2]
#     get_best_cluster = scoreDBI.index(min(scoreDBI)) + 2

#     kmeans = KMeans(n_clusters=get_best_cluster, random_state=0).fit(selected_df)
#     # kmeans = KMeans(n_clusters=get_best_cluster, random_state=0).fit(sdi)
#     query_df['kluster'] = kmeans.labels_
#     y_kmeans = kmeans.fit_predict(x_scaled)
#     centers = np.array(kmeans.cluster_centers_)

#     plt.figure(figsize=(7, 5))
#     # plt.scatter(centers[:, 0], centers[:, 1], marker="x", color='r')
#     # plt.scatter(x_scaled.iloc[:, 0], x_scaled.iloc[:, 1], c=[
#     #             plt.cm.get_cmap("Spectral")(float(i) / (int(get_best_cluster)+1)) for i in kmeans.labels_])
#     plt.scatter(centers[:, 0], centers[:, 0], marker="x", color='r')
#     plt.scatter(x_scaled, y_kmeans) 
#     # plt.scatter(x_scaled[:, 0], x_scaled[:, 0], c=[plt.cm.get_cmap("Spectral")(float(i) / (int(get_best_cluster)+1)) for i in kmeans.labels_])
#     plt.tight_layout()
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_png = buffer.getvalue()
#     buffer.close()
#     graphic = base64.b64encode(image_png)
#     graphic = graphic.decode('utf-8')
#     pylab.close()

#     # qs = qs[['State', 'Total']]
#     # arr_state = np.array(qs.iloc[:, 0])
#     # index = np.arange(36)
#     # arr_total = np.array(qs.iloc[:, 1])
#     # plt.figure(figsize=(11, 5))
#     # plt.bar(index, arr_total)
#     # plt.xlabel('State', fontsize=10)
#     # plt.ylabel('Total No of crimes', fontsize=10)
#     # plt.xticks(index, arr_state, fontsize=7, rotation=90)
#     # plt.title('Total Crime Vs State')
#     # plt.tight_layout()
#     # buffer = BytesIO()
#     # plt.savefig(buffer, format='png')
#     # buffer.seek(0)
#     # image_png = buffer.getvalue()
#     # buffer.close()
#     # graphic1 = base64.b64encode(image_png)
#     # graphic1 = graphic1.decode('utf-8')
#     # pylab.close()
#     # df = df.sort_values(by=['Crime_clusters'], ascending=True)
#     context = {
#         'title': "Applied K-Means",
#         'k': get_best_cluster,
#         'df': query_df.to_html(classes=["table-bordered", "table-striped", "table-hover", "text-center"]),
#         # 'qs': qs.to_html(classes=["table-bordered", "table-striped", "table-hover", "text-center"]),
#         'graphic': graphic,
#         # 'graphic1': graphic1,
#     }
#     return render(request, 'index.html', context)


    # plt.scatter(x_scaled, y_kmeans) 
    # plt.show()

    # kmeans = KMeans(n_clusters=get_best_cluster, random_state=0).fit(selected_df)
    # query_df['kluster'] = kmeans.labels_
    # X = selected_df['initial'].iloc[:, [x_scaled]].values





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


    # seed_random = 1
    # fitted_kmeans = {}
    # labels_kmeans = {}
    # df_scores = []
    # k_values_to_try = np.arange(2, 15)
    # for n_clusters in k_values_to_try:
    #     kmeans = KMeans(n_clusters=n_clusters, random_state=seed_random, )
    #     labels_clusters = kmeans.fit_predict(selected_df) 
    #     fitted_kmeans[n_clusters] = kmeans
    #     labels_kmeans[n_clusters] = labels_clusters
    #     db = davies_bouldin_score(selected_df, labels_clusters) 
    #     tmp_scores = {"n_clusters": n_clusters,"davies_bouldin_score": db,}
    #     df_scores.append(tmp_scores)
    # df_scores = pd.DataFrame(df_scores)
    # df_scores.set_index("n_clusters", inplace=True)

    # # kmeans = KMeans(n_clusters=n_clusters, random_state=seed_random).fit(selected_df)
    # # query_df['kluster'] = kmeans.labels_
    # kmeans = KMeans(n_clusters=n_clusters, random_state=seed_random, )
    # labels_clusters = kmeans.fit(selected_df) 
    # fitted_kmeans[n_clusters] = kmeans
    # labels_kmeans[n_clusters] = labels_clusters
    
    # plt.scatter(selected_df['initial'], selected_df['depresi'], 
    # c=[plt.cm.get_cmap("Spectral")(float(i) / (int(n_clusters)+1)) for i in kmeans.labels_], label=labels_clusters)
    # plt.xlabel('Inisialisasi: Umur, Jenis Kelamin, Status Pekerjaan, dan Jenis Depresi')
    # plt.ylabel('Jumlah Depresi')
    # plt.legend()