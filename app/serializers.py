from rest_framework import serializers
from .models import Pengguna, Pertanyaan, Jawaban, TingkatDepresi, HasilDeteksi, Penanganan, HistoryPertanyaanJawaban, Pencegahan, Artikel

class PenggunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengguna
        fields = "__all__"

class PertanyaanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pertanyaan
        fields = "__all__"

class JawabanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jawaban
        fields = "__all__"

class TingkatDepresiSerializer(serializers.ModelSerializer):
    class Meta:
        model = TingkatDepresi
        fields = "__all__"

class HasilDeteksiSerializer(serializers.ModelSerializer):
    class Meta:
        model = HasilDeteksi
        fields = "__all__"

class PenangananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Penanganan
        fields = "__all__"

class HistoryPertanyaanJawabanSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryPertanyaanJawaban
        fields = "__all__"

class PencegahanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pencegahan
        fields = "__all__"

class ArtikelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artikel
        fields = "__all__"