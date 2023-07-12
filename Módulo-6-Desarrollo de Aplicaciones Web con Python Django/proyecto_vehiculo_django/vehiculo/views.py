from django.shortcuts import render,redirect
from .forms import VehiculoForm
from . import  models


def form(request):
   if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('listado')
   else:
        form = VehiculoForm()
   return render(request, "form.html", {'form': form})
   
   
 

def listado(request):
   vehiculos=models.Vehiculo.objects.all()
   
   for vehiculo in vehiculos:
        if vehiculo.precio < 10000:
            vehiculo.condicion_precio = 'bajo'
        elif vehiculo.precio >= 10000 and vehiculo.precio < 30000:
            vehiculo.condicion_precio = 'medio'
        else:
            vehiculo.condicion_precio = 'alto'
   
   context={'vehiculos': vehiculos}
   return render(request, "listado.html", context)


