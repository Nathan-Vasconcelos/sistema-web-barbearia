from django.db import models

# Create your models here.
class Corte(models.Model):
    nome_corte = models.CharField(max_length=100)
    valor_corte = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.CharField(max_length=15)
    foto_corte = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank = True)

    def __str__(self):
        return self.nome_corte
