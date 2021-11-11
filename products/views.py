from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from.forms import RawProductForm

#def product_create_view(request):
#    my_form = RawProductForm()
#   if request.method == "POST":
#       my_form = RawProductForm(request.POST)
#    if my_form.is_valid():
#       Product.objects.create(**my_form.cleaned_data)
#    my_form = RawProductForm()
#    context = {
#        "form" : my_form
#    }
#    return render(request, "products/product_create.html", context)

def dynamic_lookup_view(request, my_id):
    obj = Product.objects.get(id=my_id)

    context = {"object": obj}
    return render(request, "products/product_detail.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../.../')
    context = {"object": obj}
    return render(request, "products/product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {"my_list": queryset}
    return render(request, "products/product_list.html", context)


