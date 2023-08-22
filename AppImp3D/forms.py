from django import forms



class ImpresoraForm (forms.Form):
    fabricante=forms.CharField(max_length=50)
    modelo=forms.CharField(max_length=50)
    diametroFilamento=forms.DecimalField(max_digits=10,decimal_places=2, label="Diámetro de Filamento",widget=forms.TextInput(attrs={'placeholder': '0.00'}), localize=True,)
    fechaDeCompra=forms.DateField(label="Fecha de Compra",
        widget=forms.DateInput(attrs={'placeholder': 'dd/mm/yyyy', 'class': 'datepicker'}),
        input_formats=['%d/%m/%Y'])
    precioArs=forms.DecimalField(max_digits=10,decimal_places=2,label= "Precio [ARS]", widget=forms.TextInput(attrs={'placeholder': '0000000000.00'}), localize=True,)

class RolloFilamentoForm(forms.Form):
    fabricante=forms.CharField(max_length=50)
    color=forms.CharField(max_length=50)
    material=forms.CharField(max_length=50)
    fechaDeCompra=forms.DateField(
        label="Fecha de Compra",
        widget=forms.DateInput(attrs={'placeholder': 'dd/mm/yyyy', 'class': 'datepicker'}),
        input_formats=['%d/%m/%Y']
    )
    precioArs=forms.DecimalField(max_digits=10,decimal_places=2,label= "Precio [ARS]", widget=forms.DateInput(attrs={'placeholder': '0000000000.00'}), localize=True,)
    dimetroFilamento=forms.DecimalField(max_digits=10,decimal_places=2, label="Diametro del Filamento", widget=forms.DateInput(attrs={'placeholder': '0.00'}),localize=True,)
    pesoGramos=forms.DecimalField(max_digits=10, decimal_places=2, label="Peso [gramos]", widget=forms.TextInput(attrs={'placeholder': '0000.00'}) , localize=True,)
    disponible=forms.BooleanField(required=False)

class Archivo3mfForm(forms.Form):
    nombreArchivo=forms.CharField(max_length=50, label="Nombre de Archivo")
    fechaCreacion=forms.DateField(
        label="Fecha de Creación",
        widget=forms.DateInput(attrs={'placeholder': 'dd/mm/yyyy', 'class': 'datepicker'}),
        input_formats=['%d/%m/%Y'])
    material=forms.CharField(max_length=50)
    tiempoImpresion=forms.TimeField(label="Tiempo de Impresión")
    pesoGramos=forms.DecimalField(max_digits=10, decimal_places=2,label="Peso [gramos]", widget=forms.DateInput(attrs={'placeholder': '0000.00'}))
    impresora=forms.CharField(max_length=50,label="Modelo de Impresora")