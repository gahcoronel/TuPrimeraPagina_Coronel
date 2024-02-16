from django import forms


class Form_Cliente(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    ciudad = forms.CharField(max_length=30)

class Form_Vendedor(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    sucursal = forms.IntegerField()

class Form_Producto(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    costo = forms.FloatField()
    stock = forms.IntegerField()