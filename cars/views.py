from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from .forms import CommentForm
from django.shortcuts import render
from .models import Car
from brands.models import Brand 

def home(request):

    brand_id = request.GET.get('brand')  
    brands = Brand.objects.all()
    
    if brand_id:
        cars = Car.objects.filter(brand_id=brand_id)
    else:
        cars = Car.objects.all()

    context = {
        'brands': brands,
        'cars': cars,
    }
    return render(request, 'home.html', context)


def car_list(request):

    brand_filter = request.GET.get('brand')
    if brand_filter:
        cars = Car.objects.filter(brand__name=brand_filter)
    else:
        cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars, 'brand_filter': brand_filter})

def car_detail(request, pk):

    car = get_object_or_404(Car, pk=pk)
    comments = car.comments.all()
    form = CommentForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        comment = form.save(commit=False)
        comment.car = car
        comment.save()
        return redirect('car_detail', pk=car.pk)

    return render(request, 'cars/car_detail.html', {'car': car, 'comments': comments, 'form': form})
