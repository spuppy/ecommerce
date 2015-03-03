import time
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse 
##^ for using with url name in urls.py
from carts.models import Cart
# Create your views here.
from .models import Order
def checkout(request):
	
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
		print cart
	except:
		the_id = None
		return HttpResponseRedirect(reverse("cart"))	

	new_order,created = Order.objects.get_or_create(cart=cart)
	if created:
		new_order.order_id = str(time.time())
		new_order.save()

	if new_order.status == "Finished":
		del request.session['cart_id']
		del request.session['items_total']
		return HttpResponseRedirect(reverse("cart"))	
	context = {}
	template = "products/home.html"

	return render(request,template,context)