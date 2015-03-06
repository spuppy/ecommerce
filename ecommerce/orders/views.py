import time
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse 
##^ for using with url name in urls.py
from carts.models import Cart
# Create your views here.
from .models import Order
from .utils import id_generator

from django.contrib.auth.decorators import login_required

def order(request):

	context = {}
	template = 'orders/user.html'
	return render(request,template,context)


@login_required
def checkout(request):
	
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
		print cart
	except:
		the_id = None
		return HttpResponseRedirect(reverse("cart"))	

	try:
		new_order = Order.objects.get(cart=cart)
	except Order.DoesNotExist:
		new_order = Order(cart=cart)
		new_order.user = request.user
		new_order.order_id = id_generator()
		new_order.save()
	except:
		return HttpResponseRedirect(reverse("cart"))			

	new_order,created = Order.objects.get_or_create(cart=cart)
	### ^  returns a tuple of the two values


	## Really need these lines ???
	if created:
		new_order.order_id =  id_generator() #str(time.time())
		new_order.save()
	new_order.user = request.user
	new_order.save()

	if new_order.status == "Finished":
		del request.session['cart_id']
		del request.session['items_total']
		return HttpResponseRedirect(reverse("cart"))	
	context = {}
	template = "products/home.html"

	return render(request,template,context)