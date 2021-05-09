from django.contrib import admin
from django.urls import path, include  # add this
from app import views
# from .views import showAll
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.conf.urls import url

urlpatterns = [
    path('list/', views.showAll, name='pertanyaan-list'),
    path('detail/<int:pk>/', views.viewPertanyaan, name='pertanyaan-detail'),
    path('create/', views.createPertanyaan, name='pertanyaan-create'),
    path('update/<int:pk>/', views.updatePertanyaan, name='pertanyaan-update '),
    path('delete/<int:pk>/', views.deletePertanyaan, name='pertanyaan-delete '),
]
