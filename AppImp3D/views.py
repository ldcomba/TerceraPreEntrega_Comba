from django.shortcuts import render

from .models import Impresora, RolloFilamento, Archivo3mf   
from django.http import HttpResponse
from .forms import ImpresoraForm, RolloFilamentoForm, Archivo3mfForm



# Create your views here.
def inicio (request):
    return render(request,"inicio.html")


def impresoras(request):
    if request.method=="POST":
        form=ImpresoraForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data

            fabricante=info["fabricante"]
            modelo=info["modelo"]
            diametroFilamento=info["diametroFilamento"]
            fechaDeCompra=info["fechaDeCompra"]
            precioArs=info["precioArs"]

            impresora=Impresora(fabricante=fabricante,modelo=modelo,diametroFilamento=diametroFilamento,fechaDeCompra=fechaDeCompra,precioArs=precioArs)
            impresora.save()
            mensaje="Impresora Agregada"
            #return render(request,"impresoras.html", {"mensaje": ,"formulario":formulario_impresora})
        else:
            mensaje="Datos Invalidos"
            #return render(request,"impresoras.html", {"mensaje": "Datos Invalidos","formulario":formulario_impresora})
    else:
        
        mensaje=""
    formulario_impresora=ImpresoraForm()
    impresoras=Impresora.objects.all()
        #return render(request,"impresoras.html",{"formulario":formulario_impresora})
    return render(request,"impresoras.html", {"mensaje": mensaje,"formulario":formulario_impresora, "impresoras":impresoras})



def rollosFilamentos(request):
    if request.method=="POST":
        form=RolloFilamentoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            rollosFilamentos=RolloFilamento(fabricante=info["fabricante"],color=info["color"],material=info["material"],fechaDeCompra=info["fechaDeCompra"],
                                            precioArs=info["precioArs"],dimetroFilamento=info["dimetroFilamento"],pesoGramos=info["pesoGramos"],disponible=info["disponible"])
            rollosFilamentos.save()
            
            mensaje="Rollo agregado"
            #return render(request,"impresoras.html", {"mensaje": "Impresora Agregada","formulario":formulario_impresora})
        else:
            mensaje="Datos Invalidos"
            #return render(request,"impresoras.html", {"mensaje": "Datos Invalidos","formulario":formulario_impresora})
    else:
        
        ##profesores=Profesor.objects.all()
        mensaje=""
    formulario_rolloFilamento=RolloFilamentoForm()
    rollosFilamentos=RolloFilamento.objects.all()
    return render(request,"rollosFilamentos.html",{"mensaje": mensaje,"formulario":formulario_rolloFilamento, "rollosFilamentos":rollosFilamentos})



def archivos3mf(request):
    if request.method=="POST":
        form=Archivo3mfForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            archivos3mf=Archivo3mf(nombreArchivo=info["nombreArchivo"],fechaCreacion=info["fechaCreacion"],material=info["material"],tiempoImpresion=info["tiempoImpresion"],
                                            pesoGramos=info["pesoGramos"],impresora=info["impresora"])
            archivos3mf.save()
            
            mensaje="Archivo agregado"
            #return render(request,"impresoras.html", {"mensaje": "Impresora Agregada","formulario":formulario_impresora})
        else:
            mensaje="Datos Invalidos"
            #return render(request,"impresoras.html", {"mensaje": "Datos Invalidos","formulario":formulario_impresora})
    else:
        
        ##profesores=Profesor.objects.all()
        mensaje=""
    formulario_archivo3mf=Archivo3mfForm()
    return render(request,"archivos3mf.html",{"mensaje": mensaje,"formulario":formulario_archivo3mf})



# class Archivo3mf(models.Model):
#     nombreArchivo=models.CharField(max_length=50)
#     fechaCreacion=models.DateField()
#     material=models.CharField(max_length=50)
#     tiempoImpresion=models.TimeField()
#     pesoGramos=models.DecimalField(max_digits=10, decimal_places=2)
#     impresoraModelo=models.CharField(max_length=50)
#     def __str__(self):
#         return f" {self.nombreArchivo} - {self.fechaCreacion} - {self.material} - {self.tiempoImpresion} - {self.pesoGramos} - {self.impresoraModelo}"