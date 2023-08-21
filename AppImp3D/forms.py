from django import forms



class ImpresoraForm (forms.Form):
    fabricante=forms.CharField(max_length=50)
    modelo=forms.CharField(max_length=50)
    diametroFilamento=forms.DecimalField(max_digits=10,decimal_places=2)
    fechaDeCompra=forms.DateField()
    precioArs=forms.DecimalField(max_digits=10,decimal_places=2)

class RolloFilamentoForm(forms.Form):
    fabricante=forms.CharField(max_length=50)
    color=forms.CharField(max_length=50)
    material=forms.CharField(max_length=50)
    fechaDeCompra=forms.DateField()
    precioArs=forms.DecimalField(max_digits=10,decimal_places=2)
    dimetroFilamento=forms.DecimalField(max_digits=10,decimal_places=2)
    pesoGramos=forms.DecimalField(max_digits=10, decimal_places=2)
    disponible=forms.BooleanField()

class Archivo3mfForm(forms.Form):
    nombreArchivo=forms.CharField(max_length=50)
    fechaCreacion=forms.DateField()
    material=forms.CharField(max_length=50)
    tiempoImpresion=forms.TimeField()
    pesoGramos=forms.DecimalField(max_digits=10, decimal_places=2)
    impresora=forms.CharField(max_length=50)