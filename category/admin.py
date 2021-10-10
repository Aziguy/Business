from django.contrib import admin
from . models import Category
from django.utils.html import format_html

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	def thumbnail(self, object):
		return format_html('<img src="{}" height="30" width="30" style="border-radius:50%;">'.format(object.cat_image.url))

	thumbnail.short_description = 'Category Image'
	list_display = ('thumbnail', 'category_name', 'slug')
	prepopulated_fields = {'slug': ('category_name',)}

admin.site.register(Category, CategoryAdmin)