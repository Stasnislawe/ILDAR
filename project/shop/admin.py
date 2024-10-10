from django.contrib import admin
from .forms import NewProductForm
from .models import Category, Product, ProductImages


class ProductImagesAdmin(admin.ModelAdmin):
  pass


class ProductImagesInline(admin.StackedInline):
  model = ProductImages
  max_num = 2
  extra = 0


admin.site.register(ProductImages, ProductImagesAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline, ]
    form = NewProductForm
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)