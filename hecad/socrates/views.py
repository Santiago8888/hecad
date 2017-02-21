from django.http import HttpResponse
from django.shortcuts import render
from .models import Car
from .forms import CarForm, CarEditForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

def index(request):
    latest_question_list = Car.objects.order_by('-fechaCompra')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'socrates/index.html', context)

@login_required(login_url='/login/login/')
def detail(request, car_id):
  if request.method == 'POST':
    instance = get_object_or_404(Car, id=car_id)
    car_form = CarEditForm(instance=instance,data=request.POST)
    if car_form.is_valid():
      car_form.save()
      car_form = get_object_or_404(Car, id=car_id)
      car_form.subTotal = car_form.valorCompra + car_form.kilometraje + car_form.electrico + car_form.mecanico + car_form.llantas + car_form.accesorios + car_form.detallado + car_form.extras+ car_form.depreciacion + car_form.costoMantenimiento
      car_form.profit = car_form.valorVenta - car_form.subTotal
      car_form.save()

  else:
    instance = get_object_or_404(Car, id=car_id)
    car_form = CarEditForm(instance=instance)
  return render(request,'socrates/detail.html',{'car_form': car_form})

def pose(request):
    if request.method == 'POST':
      car_form = CarForm(data=request.POST)
      if car_form.is_valid():
        new_car = car_form.save(commit=False)
	new_car.subTotal = new_car.valorCompra + new_car.kilometraje + new_car.electrico + new_car.mecanico + new_car.llantas + new_car.accesorios + new_car.detallado + new_car.extras+ new_car.depreciacion + new_car.costoMantenimiento
	new_car.profit = new_car.valorVenta - new_car.subTotal
	new_car.save()
    else:
      car_form = CarForm()

    return render(request, 'socrates/pose.html', {'car_form': car_form})

