from django.db import models
# Create your models here.


class ProductosTiendita(models.Model):  # Corregido el nombre del modelo
    id_producto = models.AutoField(db_column='idProducto', primary_key=True)
    name_prod = models.CharField(max_length=200)
    desc_prod = models.CharField(max_length=500)
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='idcategoria', related_name='productos')
    activo = models.IntegerField()
    precio_prod = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.id_producto)


class Categoria(models.Model):
    id_categoria   = models.AutoField(db_column='idCategoria', primary_key=True)
    name_categoria = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
      return str(self.name_categoria)
    
