from django.db import models
from datetime import *
from django.contrib.auth.models import User
from django.db.models.expressions import Value
from django.db.models.fields import DateField
from cloudinary.models import CloudinaryField

class Pengguna(models.Model):
    nama = models.CharField(max_length=255, blank = False, null = False)
    email = models.EmailField(blank = False, null = False)
    ttl = models.DateField(blank = False, null = False)
    umur = models.IntegerField(blank = False, null = False)
    jenis_kelamin = models.CharField(max_length=255, blank = False, null = False)
    pekerjaan = models.CharField(max_length=255, blank = False, null = False)
    createdAt = models.DateTimeField("Created At", auto_now=True)

    # @classmethod
    # def find_age(self):
    #     return datetime.today().date() - self.ttl
    def __str__(self):
        return self.nama

class Pertanyaan(models.Model):
    pertanyaan = models.CharField(max_length=255, blank = False, null = False)
    bobot = models.FloatField(blank = True, null = True)

    def __str__(self):
        return self.pertanyaan

class Jawaban(models.Model):
    jawaban = models.CharField(max_length=255, blank = False, null = False)
    bobot = models.FloatField(blank = True, null = True)

    def __str__(self):
        return self.jawaban

class TingkatDepresi(models.Model):
    nama_depresi = models.CharField(max_length=255, blank = False, null = False)

    def __str__(self):
        return self.nama_depresi

class HasilDeteksi(models.Model):
    pengguna = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    hasil_hitung = models.FloatField(blank = False, null = False)
    createdAt = models.DateTimeField("Created At", auto_now=True)
    tingkatdepresi = models.ForeignKey(TingkatDepresi, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pengguna)
        # return self.hasil_hitung

class Penanganan(models.Model):
    tingkatdepresi = models.ForeignKey(TingkatDepresi, on_delete=models.CASCADE)
    judul = models.CharField(max_length=255, blank = False, null = False)
    image = CloudinaryField('image')    
    isi = models.TextField(blank = False, default='')
    createdAt = models.DateTimeField("Created At", auto_now=True)

    def __str__(self):
        return self.judul

class HistoryPertanyaanJawaban(models.Model):
    hasildeteksi = models.ForeignKey(HasilDeteksi, on_delete=models.CASCADE)
    jawaban_1 = models.IntegerField(blank = False, null = False)
    jawaban_2 = models.IntegerField(blank = False, null = False)
    jawaban_3 = models.IntegerField(blank = False, null = False)
    jawaban_4 = models.IntegerField(blank = False, null = False)
    jawaban_5 = models.IntegerField(blank = False, null = False)
    jawaban_6 = models.IntegerField(blank = False, null = False)
    jawaban_7 = models.IntegerField(blank = False, null = False)
    jawaban_8 = models.IntegerField(blank = False, null = False)
    jawaban_9 = models.IntegerField(blank = False, null = False)
    jawaban_10 = models.IntegerField(blank = False, null = False)
    jawaban_11 = models.IntegerField(blank = False, null = False)
    jawaban_12 = models.IntegerField(blank = False, null = False)
    jawaban_13 = models.IntegerField(blank = False, null = False)
    jawaban_14 = models.IntegerField(blank = False, null = False)
    jawaban_15 = models.IntegerField(blank = False, null = False)
    jawaban_16 = models.IntegerField(blank = False, null = False)
    jawaban_17 = models.IntegerField(blank = False, null = False)
    jawaban_18 = models.IntegerField(blank = False, null = False)
    jawaban_19 = models.IntegerField(blank = False, null = False)
    jawaban_20 = models.IntegerField(blank = False, null = False)

    def __str__(self):
        return str(self.hasildeteksi)

# class HistoryPertanyaanJawaban(models.Model):
#     hasildeteksi = models.ForeignKey(HasilDeteksi, on_delete=models.CASCADE)
#     pertanyaan = models.ForeignKey(Pertanyaan, on_delete=models.CASCADE)
#     jawaban = models.ForeignKey(Jawaban, on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.hasildeteksi)

# class Pencegahan(models.Model):
#     judul = models.CharField(max_length=255, blank = False, null = False)
#     cover = models.CharField(max_length=255, blank = False, null = False)
#     isi = models.TextField(blank = False, default='')
#     createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
#     createdAt = models.DateTimeField("Created At", auto_now_add=True)

#     def __str__(self):
#         return self.judul

class Artikel(models.Model):
    judul = models.CharField(max_length=255, blank = False, null = False)
    image = CloudinaryField('image')
    isi = models.TextField(blank = False, default='')
    createdAt = models.DateTimeField("Created At", auto_now=True)

    def __str__(self):
        return self.judul