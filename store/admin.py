from django.contrib import admin
from . models import Product
from django.utils.html import format_html

# Register your models here.
class ProductAdmin(admin.ModelAdmin):

	def thumbnail(self, object):
		return format_html('<img src="{}" height="30" width="30" style="border-radius:50%;">'.format(object.images.url))

	list_display = ('thumbnail', 'product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
	prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)