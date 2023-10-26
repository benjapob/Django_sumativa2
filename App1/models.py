from django.db import models

# Create your models here.


class Categoria(models.Model):
    codigocategoria = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length =50)

    def __str__(self):
        return f'{str(self.codigocategoria)} {self.nombre}'

class Producto(models.Model):
    codigoproducto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    codigoBarra = models.IntegerField()
    codigocategoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.codigoproducto) + " " + self.nombre + "(PRECIO" + str(self.precio) + ")"
