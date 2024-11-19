from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_info = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name}"
    
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product
    description = models.TextField()
    stock_quantity = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"{self.name}"

    
class Order(models.Model):
    order_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')

    @property
    def total_order_price(self):
        total = sum(detail.price for detail in self.order_details.all())
        return total or 0  # Return 0 if no products are associated
    
    @property
    def total_amount(self):
        amount = self.order_details.aggregate(total=models.Sum('quantity'))['total']
        return amount or 0  # Return 0 if no products are associated
    
    @property
    def customer_name(self):
        return self.customer.name or None  # Return 0 if no products are associated
    
    def __str__(self):
        return f"Order {self.pk} - Customer {self.customer.name}"
   
class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ordered_products')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_details')
    quantity = models.IntegerField()
    
    @property
    def price(self):
        # Calculate the total price by summing the `price` field of related products
        total = self.product.price * self.quantity
        return total or 0  # Return 0 if no products are associated
        
    @property
    def product_name(self):
        return self.product.name or None  # Return 0 if no products are associated
   
    @property
    def customer_name(self):
        return self.order.customer.name or None  # Return 0 if no customers are associated
    
    def __str__(self):
        return f"#{self.pk}"
    
