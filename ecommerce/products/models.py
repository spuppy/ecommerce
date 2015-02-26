from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=120,null=False, blank=False)
	description = models.TextField(null=True,blank=True);
	price = models.DecimalField(decimal_places=2, max_digits=100, default=9.99)
	sale_price = models.DecimalField(decimal_places=2, max_digits=100, blank=True,null=True)
	#image = models.FileField(upload_to='products/images/',null=True)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)
	active = models.BooleanField(default=True)


	class Meta:
		unique_together = ('title','slug')

	def __unicode__(self):
		return str(self.title)

	def get_price(self):
		return self.price

	def get_absolute_url(self):
		return reverse("single_product", kwargs={"slug": self.slug})

class ProductImage(models.Model):
		product = models.ForeignKey(Product)
		image = models.ImageField(upload_to='products/images/')
		featured = models.BooleanField(default=False)
		thumbnail = models.BooleanField(default=False)
		updated = models.DateTimeField(auto_now_add=False,auto_now=True)
		active = models.BooleanField(default=True)

		def __unicode__(self):
			return self.product.title	

class VariationManager(models.Manager):
	# Manager allow us to customize the query sets

	def all(self):
		return super(VariationManager,self).filter(active=True)
	def sizes(self):
		return self.all().filter(category='size')
		# return super(VariationManager, self).filter(active=True).filter(category='size')
	def colors(self):
		return self.all().filter(category='color')
		# return super(VariationManager, self).filter(active=True).filter(category='color')
	def packages(self):
		return self.all().filter(category='package')
		# return super(VariationManager, self).filter(active=True).filter(category='package')	

VAR_CATEGORIES = (
		('size','size'),
		('color','color'),
		('package','package'),

	)

class Variation(models.Model):
		product = models.ForeignKey(Product)
		category = models.CharField(max_length=120,choices=VAR_CATEGORIES,default='size')
		title = models.CharField(max_length=120)
		image = models.ForeignKey(ProductImage,null=True,blank=True)
		price = models.DecimalField(max_digits=100, decimal_places=2, null=True,blank=True	)
		updated = models.DateTimeField(auto_now_add=False,auto_now=True)
		active = models.BooleanField(default=True)

		objects = VariationManager()

		def __unicode__(self):
			return self.title