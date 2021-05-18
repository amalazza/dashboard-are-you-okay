# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Pengguna, Pertanyaan, Jawaban, TingkatDepresi, HasilDeteksi, Penanganan, HistoryPertanyaanJawaban, Artikel
# Register your models here.


admin.site.register(Pengguna)
admin.site.register(Pertanyaan)
admin.site.register(Jawaban)
admin.site.register(TingkatDepresi)
admin.site.register(HasilDeteksi)
admin.site.register(Penanganan)
admin.site.register(HistoryPertanyaanJawaban)
admin.site.register(Artikel)
