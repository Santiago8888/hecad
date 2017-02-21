from .models import Car
from django import forms
class CarForm(forms.ModelForm):
  class Meta:
    model = Car
    fields = ('vehiculo', 'valorCompra', 'kilometraje', 'electrico', 'mecanico', 'llantas', 'accesorios', 'detallado', 'extras', 'depreciacion', 'costoMantenimiento','valorVenta')

class CarEditForm(forms.ModelForm):
  class Meta:
    model = Car
    fields = ('vehiculo', 'valorCompra', 'kilometraje', 'electrico', 'mecanico', 'llantas', 'accesorios', 'detallado', 'extras', 'depreciacion', 'costoMantenimiento','valorVenta')

