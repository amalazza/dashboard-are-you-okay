from django.contrib import admin
from django.urls import path, include  # add this
from app import views
# from .views import showAll
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.conf.urls import url

urlpatterns = [

    # API
    path('api-list/', views.showAll, name='pertanyaan-list'),
    path('api-detail/<int:pk>/', views.view, name='pertanyaan-detail'),
    path('api-create/', views.create, name='pertanyaan-create'),
    path('api-update/<int:pk>/', views.update, name='pertanyaan-update '),
    path('api-delete/<int:pk>/', views.delete, name='pertanyaan-delete '),

    #UI
    path('list/', views.list_view, name='pertanyaan-list'),
    path('detail/<int:id>/', views.detail_view, name='detail-pertanyaan'),
    path('tambah/', views.create_view, name='tambah-pertanyaan'),
    path('edit/<int:id>/', views.update_view, name='edit-pertanyaan'),
    path('hapus/<int:id>/', views.delete_view, name='hapus-pertanyaan'),

]
