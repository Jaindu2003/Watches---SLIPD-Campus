from django.db import models
from django.contrib.auth.models import User


class Watch(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return f"{self.brand} {self.name}"


class Profile(models.Model):
    """Extra user information saved in the database."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.watch.price * self.quantity

    def __str__(self):
        return f"{self.user.username} - {self.watch} x {self.quantity}"
