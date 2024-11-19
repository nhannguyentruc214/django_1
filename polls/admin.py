from django.contrib import admin
from .models import Customer, Product, Order, OrderDetail
from django.db.models import Count

class OrderInline(admin.StackedInline):
    model = Order
    extra = 1
    show_change_link = True

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
    show_change_link = True

class OrderDetailInline(admin.StackedInline):
    model = OrderDetail
    extra = 1
    show_change_link = True

class ProductNameFilter(admin.SimpleListFilter):
    title = 'Product Name'
    parameter_name = 'product_name'

    def lookups(self, request, model_admin):
        # Provide a list of products for filtering
        order_detail_products = Product.objects.all().values_list('id', 'name')
        return [(product_id, name) for product_id, name in order_detail_products]

    def queryset(self, request, queryset):
        # Filter queryset based on the selected product name
        if self.value():
            return queryset.filter(product__id=self.value())
        return queryset
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','address','contact_info')
    inlines = [OrderInline]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    def get_order_id(self, obj):
        return obj.id
    
    list_display = ('order_date','customer_name','get_order_id','total_amount','total_order_price')
    list_filter = ('order_date','id',)
    readonly_fields = ('total_amount','total_order_price')
    get_order_id.short_description='Order Id'
    inlines = [OrderDetailInline]

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    
    def get_order_id(self, obj):
        return obj.order_id
    
    list_display = ('product_name','customer_name', 'get_order_id','quantity','price',)
    readonly_fields = ('price',)
    get_order_id.short_description='Order Id'
    list_filter=(ProductNameFilter,)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','description','stock_quantity')
    list_filter = ('name',)
    inlines = [OrderDetailInline]

