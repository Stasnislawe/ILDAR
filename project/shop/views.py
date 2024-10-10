from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ProductImages
from cart.forms import CartAddProductForm


def product_list(request, cat_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if cat_slug:
        category = get_object_or_404(Category, slug=cat_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def categories_list(request, cat_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if cat_slug:
        category = get_object_or_404(Category, slug=cat_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/category.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})



def product_detail(request, prd_slug):
    product = get_object_or_404(Product,
                                slug=prd_slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    all_img = ProductImages.objects.all().filter(product_id=product.pk)
    return render(request,
                  'shop/product/product_detail.html',
                  {'product': product,
                  'cart_product_form': cart_product_form,
                   'all_img': all_img})