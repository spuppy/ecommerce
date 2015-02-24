from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.

from products.models import Product, Variation
from .models import Cart, CartItem

def view(request):
	try:
		the_id = request.session['cart_id']
	except:
		the_id = None
	if the_id:
		cart = Cart.objects.get(id=the_id)
		context = {'cart':cart}
	else:
		empty_message = "Your cart is empty, please keep shopping."
		context = {"empty": True, "empty_message": empty_message}

	template = 'cart/view.html'
	return render(request,template,context)

def add_to_cart(request,slug):
	request.session.set_expiry(120000) # in seconds
	
	try:
		the_id = request.session['cart_id']
	except:
		#create cart_id
		new_cart = Cart()
		new_cart.save()
		request.session['cart_id'] = new_cart.id
		the_id = new_cart.id

	cart = Cart.objects.get(id=the_id)
	
	try:
		product = Product.objects.get(slug=slug)
		#print slug
	except Product.DoesNotExists:
		pass
	except:
		pass

	product_var = [] #product variations
	if request.method == "POST":
		#print request.POST
		qty = request.POST['qty']
		for item in request.POST:
		#print item
			key = item
			val = request.POST[key]
		# print key,val
		try: 
			v = Variation.objects.get(product=product, category__iexact=key, title__iexact=val)
			### iexcact -> ignore case value
			#print v
			product_var.append(v)
		except:
			pass

		cart_item = CartItem.objects.create(cart=cart,product=product)
		# if created:
		# 	print "YES!"
	
		if len(product_var) > 0:
			cart_item.variations.add(*product_var)
			#Note put '*' => add each item in the product_var list
		cart_item.quantity = qty
		cart_item.save()
	
		new_total=0.00
		for item in cart.cartitem_set.all():
			line_total = float(item.product.price) * item.quantity
			new_total += line_total
		request.session['items_total'] = cart.cartitem_set.count()
		# print cart.products.count()
		cart.total = new_total
		cart.save()
		return HttpResponseRedirect(reverse("cart"))

	return HttpResponseRedirect(reverse("cart"))