from django.shortcuts import render, redirect
from . models import Order, OderedItem
from products.models import Product
from .models import Coustamer  
# Create your views here.

def cart(request):
    user = request.user
    customer = user.customer_profile
    cart = Order.objects.filter(owner=customer, order_status=Order.CART_SATGE).first()
    return render(request, 'cart.html', {'cart': cart})
   


# def add_to_cart(request):
#     if request.POST:
#         user = request.user
#         customer = user.customer_profile
#         quantity = int(request.POST.get('quantity'))
#         product_id = request.POST.get('product_id')
#         cart_obj, created = Order.objects.get_or_create(
#             owner = customer,
#             order_status = Order.CART_SATGE
#         )
#         product = Product.objects.get(pk=product_id)
#         ordered_item, created = OderedItem.objects.get_or_create(
#             product = product,
#             owner = cart_obj,
#             # quantity = quantity
#         )
#         if created:
#             ordered_item.quantity = quantity
#             ordered_item.save()
#         else:
#             ordered_item.quantity = ordered_item.quantity + quantity
#             ordered_item.save()
#     return redirect('cart')

def add_to_cart(request):
    if request.method == "POST":
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')

        # Get or create cart
        cart_obj = Order.objects.filter(owner=customer, order_status=Order.CART_SATGE).first()
        if not cart_obj:
            cart_obj = Order.objects.create(owner=customer, order_status=Order.CART_SATGE)

        product = Product.objects.get(pk=product_id)

        # Handle ordered item
        ordered_item = OderedItem.objects.filter(product=product, owner=cart_obj).first()
        if ordered_item:
            ordered_item.quantity += quantity
            ordered_item.save()
        else:
            OderedItem.objects.create(
                product=product,
                owner=cart_obj,
                quantity=quantity
            )

    return redirect('cart')