from django.contrib import admin

# Register your models here.
from products.models import *


class productsAdminBrandAdmin(admin.ModelAdmin):
    list_display = ['id','unique_code', 'title', 'description', 'date_created', ]


class productsAdminProductMainAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug','brand', 'price', 'date_created', ]


class productsAdminProductCartAdmin(admin.ModelAdmin):
    list_display = ['user','product', 'quantity', 'initial_price', 'final_price', 'date_created', ]


class productsAdminUserCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'price','get_products' ]


admin.site.register(productsBrandModel, productsAdminBrandAdmin)

admin.site.register(productsProductMainModel, productsAdminProductMainAdmin)
admin.site.register(productsCartModel, productsAdminProductCartAdmin)
admin.site.register(productsUserCartModel, productsAdminUserCartAdmin)
