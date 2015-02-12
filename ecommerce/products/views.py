from django.shortcuts import render

# Create your views here.

from .models import Product

def search(request):

	#print(request.GET.get('q'))
	try:
		q = request.GET.get('q')

	except:
		q = None

	if q:
		products = Product.objects.filter(title__icontains=q)
		context = {'query':q, 'products': products}
		template = 'products/results.html'
	else:
		context = {}
		template = 'products/home.html'

	return render(request, template, context)


def home(request):
	products = Product.objects.all()
	context = {'products':products}
	template = 'products/home.html'
	return render(request, template, context)

def all(request):
	products = Product.objects.all()
	context  = {'products': products}
	template = 'products/all.html'
	return render(request, template,context)

def single(request,slug):
	
	try:
		product = Product.objects.get(slug=slug) #the later id is from def single(request,id)
		images = product.productimage_set.all()
		context  = {'product': product,'images': images}
		template = 'products/single.html'
		return render(request, template,context)
	except: raise Http404
