from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name
    
class OrderHistory(models.Model):
    CHOICES = {
        "RF": "Refunded",
        "CP": "Completed",
        "CN": "Cancelled",
        "AW": "Awaiting Payment"
    }
    order_date = models.DateField()
    status = models.CharField(max_length=255, choices=CHOICES)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order_histories')

    def __str__(self):
        return f"Order {self.pk}: {self.customer.name} - {self.status}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product
    orderHistory = models.ForeignKey(OrderHistory, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

