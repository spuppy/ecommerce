from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),	
    url(r'^$', 'products.views.home', name='home'),
    url(r'^cart/(?P<id>\d+)/$', 'carts.views.remove_from_cart', name='remove_from_cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$', 'carts.views.add_to_cart', name='add_to_cart'),
    url(r'^cart/$', 'carts.views.view', name='cart'),
    url(r'^checkout/$', 'orders.views.checkout', name='checkout'),
    url(r'^s/$', 'products.views.search', name='search'),
    url(r'^products/$', 'products.views.all', name='products'),
    url(r'^products/(?P<slug>[\w-]+)/$', 'products.views.single', name='single_product'),
    url(r'^orders/$', 'orders.views.order', name='user_orders'),
    #Note \d+ == only digit

    #url(r'^products/(?P<slug>.*)/$', 'products.views.single', name='single_product'),
    url(r'^admin/', include(admin.site.urls)),

) #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)