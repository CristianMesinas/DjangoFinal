from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=25, null=False)
    precio = models.FloatField()
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    