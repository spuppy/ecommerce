#from django.core.uslresolvers import reverse
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

	#def get_absoluteurl(self):
	#	return reverse("single_product", kwargs={"slug": self.slug})

class ProductImage(models.Model):
		product = models.ForeignKey(Product)
		image = models.ImageField(upload_to='products/images/')
		featured = models.BooleanField(default=False)
		thumbnail = models.BooleanField(default=False)
		updated = models.DateTimeField(auto_now_add=False,auto_now=True)
		active = models.BooleanField(default=True)

		def __unicode__(self):
			return self.product.title	