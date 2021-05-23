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


    # path('coba/', views.clustering_data, name='coba'),

    # PENGGUNA API
    path('', views.apiOverviewPengguna, name='apiOverviewPengguna'),
    path('pengguna-list/', views.showAllPengguna, name='pengguna-list'),
    path('pengguna-detail/<int:pk>/', views.viewPengguna, name='pengguna-detail'),
    path('pengguna-detail-byemail/<str:email>/', views.viewEmailPengguna, name='pengguna-detail-byemail'),
    path('pengguna-create/', views.createPengguna, name='pengguna-create'),
    path('pengguna-update/<int:pk>/', views.updatePengguna, name='pengguna-update '),
    path('pengguna-delete/<int:pk>/', views.deletePengguna, name='pengguna-delete '),
    # PENGGUNA CRUD
    path('', views.overviewPengguna, name='overviewPengguna'),
    path('app/pengguna/list/', views.list_view_pengguna, name='list-pengguna'),
    path('app/pengguna/detail/<int:id>/', views.detail_view_pengguna, name='detail-pengguna'),
    path('app/pengguna/tambah/', views.create_view_pengguna, name='tambah-pengguna'),
    path('app/pengguna/edit/<int:id>/', views.update_view_pengguna, name='edit-pengguna'),
    path('app/pengguna/hapus/<int:id>/', views.delete_view_pengguna, name='hapus-pengguna'),




    # PERTANYAAN API
    path('', views.apiOverviewPertanyaan, name='apiOverviewPertanyaan'),
    path('pertanyaan-list/', views.showAllPertanyaan, name='pertanyaan-list'),
    path('pertanyaan-detail/<int:pk>/', views.viewPertanyaan, name='pertanyaan-detail'),
    path('pertanyaan-create/', views.createPertanyaan, name='pertanyaan-create'),
    path('pertanyaan-update/<int:pk>/', views.updatePertanyaan, name='pertanyaan-update '),
    path('pertanyaan-delete/<int:pk>/', views.deletePertanyaan, name='pertanyaan-delete '),
    # PERTANYAAN CRUD
    path('', views.overviewPertanyaan, name='overviewPertanyaan'),
    path('layanan/kuesioner/pertanyaan/list/', views.list_view_pertanyaan, name='list-pertanyaan'),
    path('layanan/kuesioner/pertanyaan/detail/<int:id>/', views.detail_view_pertanyaan, name='detail-pertanyaan'),
    path('layanan/kuesioner/pertanyaan/tambah/', views.create_view_pertanyaan, name='tambah-pertanyaan'),
    path('layanan/kuesioner/pertanyaan/edit/<int:id>/', views.update_view_pertanyaan, name='edit-pertanyaan'),
    path('layanan/kuesioner/pertanyaan/hapus/<int:id>/', views.delete_view_pertanyaan, name='hapus-pertanyaan'),




    # JAWABAN API
    path('', views.apiOverviewJawaban, name='apiOverviewJawaban'),
    path('jawaban-list/', views.showAllJawaban, name='jawaban-list'),
    path('jawaban-detail/<int:pk>/', views.viewJawaban, name='jawaban-detail'),
    path('jawaban-create/', views.createJawaban, name='jawaban-create'),
    path('jawaban-update/<int:pk>/', views.updateJawaban, name='jawaban-update '),
    path('jawaban-delete/<int:pk>/', views.deleteJawaban, name='jawaban-delete '),
    # JAWABAN CRUD
    path('', views.overviewJawaban, name='overviewJawaban'),
    path('layanan/kuesioner/jawaban/list/', views.list_view_jawaban, name='list-jawaban'),
    path('layanan/kuesioner/jawaban/detail/<int:id>/', views.detail_view_jawaban, name='detail-jawaban'),
    path('layanan/kuesioner/jawaban/tambah/', views.create_view_jawaban, name='tambah-jawaban'),
    path('layanan/kuesioner/jawaban/edit/<int:id>/', views.update_view_jawaban, name='edit-jawaban'),
    path('layanan/kuesioner/jawaban/hapus/<int:id>/', views.delete_view_jawaban, name='hapus-jawaban'),




    # TINGKAT DEPRESI API
    path('', views.apiOverviewTingkatDepresi, name='apiOverviewTingkatDepresi'),
    path('tingkatdepresi-list/', views.showAllTingkatDepresi, name='tingkatdepresi-list'),
    path('tingkatdepresi-detail/<int:pk>/', views.viewTingkatDepresi, name='tingkatdepresi-detail'),
    path('tingkatdepresi-create/', views.createTingkatDepresi, name='tingkatdepresi-create'),
    path('tingkatdepresi-update/<int:pk>/', views.updateTingkatDepresi, name='tingkatdepresi-update '),
    path('tingkatdepresi-delete/<int:pk>/', views.deleteTingkatDepresi, name='tingkatdepresi-delete '),




    # HASIL DETEKSI API
    path('', views.apiOverviewHasilDeteksi, name='apiOverviewHasilDeteksi'),
    path('hasildeteksi-list/', views.showAllHasilDeteksi, name='hasildeteksi-list'),
    path('hasildeteksi-detail/<int:pk>/', views.viewHasilDeteksi, name='hasildeteksi-detail'),
    path('hasildeteksi-detail-by-idpengguna/<int:pengguna_id>/', views.viewIdPenggunaHasilDeteksi, name='hasildeteksi-detail-by-idpengguna'),
    path('hasildeteksi-detail-by-recentidpengguna/<int:pengguna_id>/', views.viewRecentIdPenggunaHasilDeteksi, name='hasildeteksi-detail-by-recentidpengguna'),
    path('hasildeteksi-create/', views.createHasilDeteksi, name='hasildeteksi-create'),
    path('hasildeteksi-update/<int:pk>/', views.updateHasilDeteksi, name='hasildeteksi-update '),
    path('hasildeteksi-delete/<int:pk>/', views.deleteHasilDeteksi, name='hasildeteksi-delete '),




    # PENANGANAN API
    path('', views.apiOverviewPenanganan, name='apiOverviewPenanganan'),
    path('penanganan-list/', views.showAllPenanganan, name='penanganan-list'),
    path('penanganan-detail/<int:pk>/', views.viewPenanganan, name='penanganan-detail'),
    path('penanganan-detail-by-idtingkatdepresi/<int:tingkatdepresi_id>/', views.viewIdTingkatDepresiPenanganan, name='penanganan-detail-by-idtingkatdepresi'),
    path('penanganan-create/', views.createPenanganan, name='penanganan-create'),
    path('penanganan-update/<int:pk>/', views.updatePenanganan, name='penanganan-update '),
    path('penanganan-delete/<int:pk>/', views.deletePenanganan, name='penanganan-delete '),
    # PENANGANAN CRUD
    path('', views.overviewPenanganan, name='overviewPenanganan'),
    path('layanan/penanganan/list/', views.list_view_penanganan, name='list-penanganan'),
    path('layanan/penanganan/detail/<int:id>/', views.detail_view_penanganan, name='detail-penanganan'),
    path('layanan/penanganan/tambah/', views.create_view_penanganan, name='tambah-penanganan'),
    path('layanan/penanganan/edit/<int:id>/', views.update_view_penanganan, name='edit-penanganan'),
    path('layanan/penanganan/hapus/<int:id>/', views.delete_view_penanganan, name='hapus-penanganan'),




    # HISTORY PERTANYAAN JAWABAN API
    path('', views.apiOverviewHistoryPertanyaanJawaban, name='apiOverviewHistoryPertanyaanJawaban'),
    path('historypertanyaanjawaban-list/', views.showAllHistoryPertanyaanJawaban, name='historypertanyaanjawaban-list'),
    path('historypertanyaanjawaban-detail/<int:pk>/', views.viewHistoryPertanyaanJawaban, name='historypertanyaanjawaban-detail'),
    path('historypertanyaanjawaban-create/', views.createHistoryPertanyaanJawaban, name='historypertanyaanjawaban-create'),
    path('historypertanyaanjawaban-update/<int:pk>/', views.updateHistoryPertanyaanJawaban, name='historypertanyaanjawaban-update '),
    path('historypertanyaanjawaban-delete/<int:pk>/', views.deleteHistoryPertanyaanJawaban, name='historypertanyaanjawaban-delete '),




    # ARTIKEL API
    path('', views.apiOverviewArtikel, name='apiOverviewArtikel'),
    path('artikel-list/', views.showAllArtikel, name='artikel-list'),
    path('artikel-detail/<int:pk>/', views.viewArtikel, name='artikel-detail'),
    path('artikel-create/', views.createArtikel, name='artikel-create'),
    path('artikel-update/<int:pk>/', views.updateArtikel, name='artikel-update '),
    path('artikel-delete/<int:pk>/', views.deleteArtikel, name='artikel-delete '),
    # ARTIKEL CRUD
    path('', views.overviewArtikel, name='overviewArtikel'),
    path('layanan/artikel/list/', views.list_view_artikel, name='list-artikel'),
    path('layanan/artikel/detail/<int:id>/', views.detail_view_artikel, name='detail-artikel'),
    path('layanan/artikel/tambah/', views.create_view_artikel, name='tambah-artikel'),
    path('layanan/artikel/edit/<int:id>/', views.update_view_artikel, name='edit-artikel'),
    path('layanan/artikel/hapus/<int:id>/', views.delete_view_artikel, name='hapus-artikel'),

]
