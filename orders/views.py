from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order
from cars.models import Car

@login_required
def place_order(request, car_id):
    """
    Place an order for a car.
    """
    car = Car.objects.get(pk=car_id)
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        Order.objects.create(user=request.user, car=car, quantity=1)
        messages.success(request, "Order placed successfully!")
    else:
        messages.error(request, "Sorry, this car is out of stock.")
    return redirect('car_detail', pk=car_id)

@login_required
def order_history(request):
    """
    Display all orders for the logged-in user.
    """
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_history.html', {'orders': orders})
