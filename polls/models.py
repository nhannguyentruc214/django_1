from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product
    description = models.TextField()
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

    @property
    def total_order_value(self):
        # Calculate the total value by summing the `value` field of related products
        # total = self.orderDetails.aggregate(total=models.Sum('total_quantity_value'))['total']
        total = sum(detail.total_quantity_value for detail in self.orderDetails.all())
        return total or 0  # Return 0 if no products are associated
    
    @property
    def total_ammount(self):
        # Calculate the total value by summing the `value` field of related products
        ammount = self.orderDetails.aggregate(total=models.Sum('quantity'))['total']
        return ammount or 0  # Return 0 if no products are associated
    
    def __str__(self):
        return f"Order {self.pk}: {self.customer.name} - {self.status}"
   
class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ordered_products')
    orderHistory = models.ForeignKey(OrderHistory, on_delete=models.CASCADE, related_name='orderDetails')
    quantity = models.IntegerField()
    
    @property
    def total_quantity_value(self):
        # Calculate the total value by summing the `value` field of related products
        total = self.product.value * self.quantity
        return total or 0  # Return 0 if no products are associated
        
    @property
    def product_name(self):
        return self.product.name or None  # Return 0 if no products are associated

    def __str__(self):
        return f"Order detail"
    
