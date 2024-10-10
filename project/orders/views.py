from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm, WithoutDeliveryForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        form2 = WithoutDeliveryForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
                cart.clear()
                return render(request, 'orders/order/created.html',
                              {'order': order})
    else:
        if cart:
            form = OrderCreateForm
            return render(request, 'orders/order/create.html',
                          {'cart': cart, 'form': form})
    return render(request, 'orders/order/cartisempty.html')
