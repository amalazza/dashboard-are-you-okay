# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

    path('', views.apiOverviewPengguna, name='apiOverviewPengguna'),
    path('pengguna-list/', views.showAllPengguna, name='pengguna-list'),

    path('', views.apiOverviewPertanyaan, name='apiOverviewPertanyaan'),
    path('pertanyaan-list/', views.showAllPertanyaan, name='pertanyaan-list'),

    path('', views.apiOverviewJawaban, name='apiOverviewJawaban'),
    path('jawaban-list/', views.showAllJawaban, name='jawaban-list'),

    path('', views.apiOverviewTingkatDepresi, name='apiOverviewTingkatDepresi'),
    path('tingkatdepresi-list/', views.showAllTingkatDepresi, name='tingkatdepresi-list'),

    path('', views.apiOverviewHasilDeteksi, name='apiOverviewHasilDeteksi'),
    path('hasildeteksi-list/', views.showAllHasilDeteksi, name='hasildeteksi-list'),

    path('', views.apiOverviewPenanganan, name='apiOverviewPenanganan'),
    path('penanganan-list/', views.showAllPenanganan, name='penanganan-list'),

    path('', views.apiOverviewHistoryPertanyaanJawaban, name='apiOverviewHistoryPertanyaanJawaban'),
    path('historypertanyaanjawaban-list/', views.showAllHistoryPertanyaanJawaban, name='historypertanyaanjawaban-list'),

    path('', views.apiOverviewPencegahan, name='apiOverviewPencegahan'),
    path('pencegahan-list/', views.showAllPencegahan, name='pencegahan-list'),

    path('', views.apiOverviewArtikel, name='apiOverviewArtikel'),
    path('artikel-list/', views.showAllArtikel, name='artikel-list'),

]
