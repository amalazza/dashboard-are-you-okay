# Generated by Django 3.2.1 on 2021-05-18 02:13

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('isi', models.TextField(default='')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='HasilDeteksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pengguna_id', models.IntegerField()),
                ('hasil_hitung', models.FloatField()),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('tingkatdepresi_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HistoryPertanyaanJawaban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hasildeteksi_id', models.IntegerField()),
                ('pertanyaan_id', models.IntegerField()),
                ('jawaban_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jawaban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jawaban', models.CharField(max_length=255)),
                ('bobot', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Penanganan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tingkatdepresi_id', models.IntegerField()),
                ('judul', models.CharField(max_length=255)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('isi', models.TextField(default='')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='Pengguna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('ttl', models.DateField()),
                ('jenis_kelamin', models.CharField(max_length=255)),
                ('pekerjaan', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='Pertanyaan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pertanyaan', models.CharField(max_length=255)),
                ('bobot', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TingkatDepresi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_depresi', models.CharField(max_length=255)),
            ],
        ),
    ]
