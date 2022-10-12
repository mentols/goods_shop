from django.contrib import admin

from clothes.models import Warehouse, Good, Category, Content, Address, Order, Customer


# Register your models here.
@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("category_name",)}


class AdminGood(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("goods_name",)}


admin.site.register(Warehouse)
admin.site.register(Good, AdminGood)
# admin.site.register(Category, AdminCategory)
admin.site.register(Content)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(Customer)
