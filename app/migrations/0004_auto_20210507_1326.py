# Generated by Django 3.2.1 on 2021-05-07 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_historypertanyaanjawaban_jawaban_pertanyaan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artikel',
            name='createdBy',
        ),
        migrations.RemoveField(
            model_name='hasildeteksi',
            name='pengguna',
        ),
        migrations.RemoveField(
            model_name='historypertanyaanjawaban',
            name='HasilDeteksi',
        ),
        migrations.RemoveField(
            model_name='historypertanyaanjawaban',
            name='Jawaban',
        ),
        migrations.RemoveField(
            model_name='historypertanyaanjawaban',
            name='Pertanyaan',
        ),
        migrations.RemoveField(
            model_name='penanganan',
            name='createdBy',
        ),
        migrations.RemoveField(
            model_name='penanganan',
            name='tingkat_depresi',
        ),
        migrations.RemoveField(
            model_name='pencegahan',
            name='createdBy',
        ),
        migrations.AddField(
            model_name='artikel',
            name='createdBy_id',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='hasildeteksi',
            name='pengguna_id',
            field=models.IntegerField(default=''),
        ),
        migrations.AddField(
            model_name='historypertanyaanjawaban',
            name='HasilDeteksi_id',
            field=models.IntegerField(default=''),
        ),
        migrations.AddField(
            model_name='historypertanyaanjawaban',
            name='Jawaban_id',
            field=models.IntegerField(default=''),
        ),
        migrations.AddField(
            model_name='historypertanyaanjawaban',
            name='Pertanyaan_id',
            field=models.IntegerField(default=''),
        ),
        migrations.AddField(
            model_name='penanganan',
            name='createdBy_id',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='penanganan',
            name='tingkat_depresi_id',
            field=models.IntegerField(default=''),
        ),
        migrations.AddField(
            model_name='pencegahan',
            name='createdBy_id',
            field=models.IntegerField(default='1'),
        ),
    ]
