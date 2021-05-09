from django.contrib import admin
from django.urls import path, include  # add this
from app import views
# from .views import showAll
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.conf.urls import url

urlpatterns = [
    # path('pertanyaan-list/', views.showAll, name='pertanyaan-list'),
    path('api/', views.ApiView.as_view(), name='pertanyaan-list'),
]
