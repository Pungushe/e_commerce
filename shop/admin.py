from django.contrib import admin

from . models import OrderDetail, Product


admin.site.site_header = "Pro-Shop"
admin.site.site_title = "Pro-Shop"
admin.site.index_title = "Добро пожаловать Pro-Shop"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name',)
    list_editable = ('price', )
    actions=('make_zero',)
    
    def make_zero(self, request, queryset):
        queryset.update(price=0)


admin.site.register(Product, ProductAdmin)
admin.site.register(OrderDetail)


