# VENTAJA: se evita tener que agregar campo por campo cada detalle que estemos precisando
# DESVENTAJA: no tiene estilos, por lo cual hay q aplicarselos con css

from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Productos
        fields = ('nombre','precio','stock','categoria')
    