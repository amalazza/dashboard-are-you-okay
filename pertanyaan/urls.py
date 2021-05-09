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
    path('detail/<int:pk>/', views.view, name='pertanyaan-detail'),
    path('create/', views.create, name='pertanyaan-create'),
    path('update/<int:pk>/', views.update, name='pertanyaan-update '),
    path('delete/<int:pk>/', views.delete, name='pertanyaan-delete '),
]
