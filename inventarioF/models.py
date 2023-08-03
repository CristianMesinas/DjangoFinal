from django.db import models

# Create your models here.
class Categorias(models.Model):
    nombre = models.CharField(max_length=20, null=False)
    
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Productos(models.Model):
    nombre = models.CharField(max_length=25, null=False)
    precio = models.FloatField()
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, default=1)
    #se debe colocar antes la class categorias para que la foreingKey lo reconozca
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
    