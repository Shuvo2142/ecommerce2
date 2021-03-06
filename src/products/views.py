from django.views.generic import DetailView
from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Product


class ProductDetailView(DetailView):
	model = Product 
	# template_name = <app_name>/<modelname>_detail.html************this is default*******



def product_detail_view_func(request, id):
	product_instance = get_object_or_404(Product, id=id)
	try:
		product_instance = Product.objects.get(id=id)
	except Product.DoesNotExist:
		raise Http404
	except:
		raise Http404	

	template = "products/product_detail.html"
	context = {
		"object": product_instance
	}

	return render(request, template, context)
