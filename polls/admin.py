from django.contrib import admin
from .models import Customer, Product, OrderHistory, OrderDetail
from django.db.models import Count

class OrderInline(admin.StackedInline):
    model = OrderHistory
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
    list_display = ('name','address')
    inlines = [OrderInline]

@admin.register(OrderHistory)
class OrderHistoryAdmin(admin.ModelAdmin):

    list_display = ('order_date','id','status','total_ammount','total_order_value')
    list_filter = ('order_date','id','status')
    readonly_fields = ('total_ammount','total_order_value')
    inlines = [OrderDetailInline]

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    
    def get_order_history_id(self, obj):
        return obj.orderHistory_id
    
    list_display = ('product_name', 'get_order_history_id','quantity','total_quantity_value',)
    readonly_fields = ('product_name', 'orderHistory_id','total_quantity_value',)
    get_order_history_id.short_description='Order History Id'
    list_filter=(ProductNameFilter,)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','value','description')
    list_filter = ('name',)
    inlines = [OrderDetailInline]

