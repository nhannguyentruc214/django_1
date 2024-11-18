from django.contrib import admin
from .models import Customer, Product, OrderHistory
from django.db.models import Count

class OrderInline(admin.StackedInline):
    model = OrderHistory
    extra = 1
    show_change_link = True

class ProductInline(admin.StackedInline):
    model = Product
    extra = 1
    show_change_link = True

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','address')
    inlines = [OrderInline]

@admin.register(OrderHistory)
class OrderHistoryAdmin(admin.ModelAdmin):

    def product_count(self, obj):
            return obj.products.count()
    
    list_display = ('order_date','status','product_count','total_value')
    list_filter = ('order_date','status')
    readonly_fields = ('product_count','total_value')
    product_count.short_description = 'Number of Products'

    inlines = [ProductInline]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','value')
