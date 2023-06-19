from django.contrib import admin
from .models import Product , Category , Cart
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    pass
class CategoryAdmin(admin.ModelAdmin):
    pass
class CartAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product , ProductAdmin)
admin.site.register(Category , CategoryAdmin)
admin.site.register(Cart , CartAdmin)