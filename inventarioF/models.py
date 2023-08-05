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

procedencia = [('Nacional','NAC'), ('IMP', 'Importado')] #tupla que indicara que origen es un select

class Productos(models.Model):
    nombre = models.CharField(max_length=25, null=False)
    precio = models.FloatField()
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, default=1)
    #se debe colocar antes la class categorias para que la foreingKey lo reconozca
    NACIONAL = "NAC"
    IMPORTADO = "IMP"
    procedencia = (NACIONAL, "Nacional"), (IMPORTADO, "Importado")
    origen = models.CharField(max_length=20, choices = procedencia)
    
    def is_upperclass(self):
        return self.origen in {self.NACIONAL, self.IMPORTADO}
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
    