from django.db import models
from django.contrib.auth.models import User

class Pengguna(models.Model):
    nama = models.CharField(max_length=255, blank = False, null = False)
    email = models.EmailField(blank = False, null = False)
    ttl = models.DateField(blank = False, null = False)
    jenis_kelamin = models.CharField(max_length=255, blank = False, null = False)
    pekerjaan = models.CharField(max_length=255, blank = False, null = False)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.nama

class Pertanyaan(models.Model):
    pertanyaan = models.CharField(max_length=255, blank = False, null = False)

    def __str__(self):
        return self.pertanyaan

class Jawaban(models.Model):
    jawaban = models.CharField(max_length=255, blank = False, null = False)

    def __str__(self):
        return self.jawaban

class TingkatDepresi(models.Model):
    nama_depresi = models.CharField(max_length=255, blank = False, null = False)

    def __str__(self):
        return self.nama_depresi

# class HasilDeteksi(models.Model):
#     pengguna = models.ForeignKey(Pengguna, on_delete=models.CASCADE, blank=False, null=False, related_name='hasildeteksi')
#     hasil_hitung = models.FloatField(blank = False, null = False)
#     createdAt = models.DateTimeField("Created At", auto_now_add=True)

#     def __str__(self):
#         return self.hasil_hitung

class HasilDeteksi(models.Model):
    pengguna_id = models.IntegerField(blank = False, null = False)
    hasil_hitung = models.FloatField(blank = False, null = False)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.hasil_hitung

class Penanganan(models.Model):
    tingkat_depresi_id = models.IntegerField(blank = False, null = False)
    judul = models.CharField(max_length=255, blank = False, null = False)
    cover = models.CharField(max_length=255, blank = False, null = False)
    isi = models.TextField(blank = False, default='')
    createdBy_id = models.IntegerField(blank = False, null = False, default='1')
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.judul

class HistoryPertanyaanJawaban(models.Model):
    HasilDeteksi_id = models.IntegerField(blank = False, null = False)
    Pertanyaan_id = models.IntegerField(blank = False, null = False)
    Jawaban_id = models.IntegerField(blank = False, null = False)

    def __str__(self):
        return self.HasilDeteksi_id

class Pencegahan(models.Model):
    judul = models.CharField(max_length=255, blank = False, null = False)
    cover = models.CharField(max_length=255, blank = False, null = False)
    isi = models.TextField(blank = False, default='')
    createdBy_id = models.IntegerField(blank = False, null = False, default='1')
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.judul

class Artikel(models.Model):
    judul = models.CharField(max_length=255, blank = False, null = False)
    cover = models.CharField(max_length=255, blank = False, null = False)
    isi = models.TextField(blank = False, default='')
    createdBy_id = models.IntegerField(blank = False, null = False, default='1')
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.judul