from django.shortcuts import render, redirect, get_object_or_404
from . models import Order, OderedItem
from django.contrib import messages
from products.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.

def cart(request):
    user = request.user
    customer = user.customer_profile
    cart = Order.objects.filter(owner=customer, order_status=Order.CART_STAGE).first()
    return render(request, 'cart.html', {'cart': cart})
   

def add_to_cart(request):
    if request.method == "POST":
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')

        # Get or create cart
        cart_obj = Order.objects.filter(owner=customer, order_status=Order.CART_STAGE).first()
        if not cart_obj:
            cart_obj = Order.objects.create(owner=customer, order_status=Order.CART_STAGE)

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

def checkout_cart(request):
    if request.method == "POST":
        try:
            user = request.user
            customer = user.customer_profile
            total = float(request.POST.get('total'))

            order_obj = Order.objects.filter(
                owner=customer,
                order_status=Order.CART_STAGE
            ).first()

            if order_obj:
                order_obj.order_status = Order.ORDER_CONFIRMED
                order_obj.total_price = total
                order_obj.save()
                messages.success(request, "Your order is processed.")
            else:
                messages.warning(request, "No order found to process.")
        except Exception as e:
            print("Checkout Error:", e)
            messages.error(request, f"Error: {e}")

    return redirect('cart')

def remove_item_from_cart(request, pk):
    item = get_object_or_404(OderedItem, pk=pk)
    item.delete()
    return redirect('cart')

@login_required(login_url='account')
def view_orders(request):
    user = request.user
    customer = user.customer_profile
    cart = Order.objects.filter(owner=customer, order_status=Order.CART_STAGE).first()
    return render(request, 'cart.html', {'cart': cart})

@login_required(login_url='account')
def show_orders(request):
    user = request.user
    customer = user.customer_profile
    all_orders = Order.objects.filter(owner = customer).exclude(order_status = Order.CART_STAGE)
    context = {'orders':all_orders}
    return render(request, 'orders.html', context) 