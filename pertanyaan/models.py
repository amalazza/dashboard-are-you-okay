from django.db import models

# Create your models here.
class Pertanyaan(models.Model):
    # id_pertanyaan = models.BigAutoField(primary_key=True)
    pertanyaan = models.CharField(max_length=255)
    bobot = models.FloatField(blank = True, null = True)

    def __str__(self):
        return str(self.pertanyaan)