from django.db import models
from brands.models import Brand
from django.contrib.auth.models import User

class Car(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cars/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="cars")

    def __str__(self):
        return f"{self.name} ({self.brand.name})"

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.car.name}"
