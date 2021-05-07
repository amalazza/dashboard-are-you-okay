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
    path('pengguna-detail/<int:pk>/', views.viewPengguna, name='pengguna-detail'),
    path('pengguna-create/', views.createPengguna, name='pengguna-create'),
    path('pengguna-update/<int:pk>/', views.updatePengguna, name='pengguna-update '),
    path('pengguna-delete/<int:pk>/', views.deletePengguna, name='pengguna-delete '),

    path('', views.apiOverviewPertanyaan, name='apiOverviewPertanyaan'),
    path('pertanyaan-list/', views.showAllPertanyaan, name='pertanyaan-list'),
    path('pertanyaan-detail/<int:pk>/', views.viewPertanyaan, name='pertanyaan-detail'),
    path('pertanyaan-create/', views.createPertanyaan, name='pertanyaan-create'),
    path('pertanyaan-update/<int:pk>/', views.updatePertanyaan, name='pertanyaan-update '),
    path('pertanyaan-delete/<int:pk>/', views.deletePertanyaan, name='pertanyaan-delete '),

    path('', views.apiOverviewJawaban, name='apiOverviewJawaban'),
    path('jawaban-list/', views.showAllJawaban, name='jawaban-list'),
    path('jawaban-detail/<int:pk>/', views.viewJawaban, name='jawaban-detail'),
    path('jawaban-create/', views.createJawaban, name='jawaban-create'),
    path('jawaban-update/<int:pk>/', views.updateJawaban, name='jawaban-update '),
    path('jawaban-delete/<int:pk>/', views.deleteJawaban, name='jawaban-delete '),

    path('', views.apiOverviewTingkatDepresi, name='apiOverviewTingkatDepresi'),
    path('tingkatdepresi-list/', views.showAllTingkatDepresi, name='tingkatdepresi-list'),
    path('tingkatdepresi-detail/<int:pk>/', views.viewTingkatDepresi, name='tingkatdepresi-detail'),
    path('tingkatdepresi-create/', views.createTingkatDepresi, name='tingkatdepresi-create'),
    path('tingkatdepresi-update/<int:pk>/', views.updateTingkatDepresi, name='tingkatdepresi-update '),
    path('tingkatdepresi-delete/<int:pk>/', views.deleteTingkatDepresi, name='tingkatdepresi-delete '),

    path('', views.apiOverviewHasilDeteksi, name='apiOverviewHasilDeteksi'),
    path('hasildeteksi-list/', views.showAllHasilDeteksi, name='hasildeteksi-list'),
    path('hasildeteksi-detail/<int:pk>/', views.viewHasilDeteksi, name='hasildeteksi-detail'),
    path('hasildeteksi-create/', views.createHasilDeteksi, name='hasildeteksi-create'),
    path('hasildeteksi-update/<int:pk>/', views.updateHasilDeteksi, name='hasildeteksi-update '),
    path('hasildeteksi-delete/<int:pk>/', views.deleteHasilDeteksi, name='hasildeteksi-delete '),

    path('', views.apiOverviewPenanganan, name='apiOverviewPenanganan'),
    path('penanganan-list/', views.showAllPenanganan, name='penanganan-list'),
    path('penanganan-detail/<int:pk>/', views.viewPenanganan, name='penanganan-detail'),
    path('penanganan-create/', views.createPenanganan, name='penanganan-create'),
    path('penanganan-update/<int:pk>/', views.updatePenanganan, name='penanganan-update '),
    path('penanganan-delete/<int:pk>/', views.deletePenanganan, name='penanganan-delete '),

    path('', views.apiOverviewHistoryPertanyaanJawaban, name='apiOverviewHistoryPertanyaanJawaban'),
    path('historypertanyaanjawaban-list/', views.showAllHistoryPertanyaanJawaban, name='historypertanyaanjawaban-list'),
    path('historypertanyaanjawaban-detail/<int:pk>/', views.viewHistoryPertanyaanJawaban, name='historypertanyaanjawaban-detail'),
    path('historypertanyaanjawaban-create/', views.createHistoryPertanyaanJawaban, name='historypertanyaanjawaban-create'),
    path('historypertanyaanjawaban-update/<int:pk>/', views.updateHistoryPertanyaanJawaban, name='historypertanyaanjawaban-update '),
    path('historypertanyaanjawaban-delete/<int:pk>/', views.deleteHistoryPertanyaanJawaban, name='historypertanyaanjawaban-delete '),

    path('', views.apiOverviewPencegahan, name='apiOverviewPencegahan'),
    path('pencegahan-list/', views.showAllPencegahan, name='pencegahan-list'),

    path('', views.apiOverviewArtikel, name='apiOverviewArtikel'),
    path('artikel-list/', views.showAllArtikel, name='artikel-list'),

]
