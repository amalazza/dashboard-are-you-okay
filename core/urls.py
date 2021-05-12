from django.contrib import admin
from django.urls import path, include  # add this
from app import views
from app.views import *
# from django.conf import settings
# from django.conf.urls.static import static
import os

urlpatterns = [
    # path('', admin.site.urls),          # Django admin route
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")), # Auth routes - login / register
    # path("", include("app.urls")),             # UI Kits Html files
    # path("layanan/kuesioner/pertanyaan/", include("pertanyaan.urls")), 
    path("", include(('app.urls', 'app'), namespace='app')), 

    # path('preprocessing/', preprocessing, name='preprocessing'),
    # path('checker_page/', checker_page, name='checker_page'),
    # path('chooseMethod/', chooseMethod, name='chooseMethod'),
    # path('classification/', classification, name='classification'),
    # path('clustering/', clustering, name='clustering'),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
