from django.db import models

# Create your models here.
class Pertanyaan(models.Model):
    # id_pertanyaan = models.BigAutoField(primary_key=True)
    pertanyaan = models.CharField(max_length=255)

    def __str__(self):
        return str(self.pertanyaan)