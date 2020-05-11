from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm, RawProductForm


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/product_list.html', context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # POST request
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
        # alternatively - setting manually all parameters;
        # 'title': obj.title,
        # 'summary': obj.summary,
        # 'price': obj.price
        #  etc.
    }
    return render(request, 'products/product_delete.html', context)


def dynamic_lookup_view(request, my_id):
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExists:
        raise Http404
    # OR - faster than try block is get_objext_or_404, only 1 line:
    # obj = get_objext_or_404(Product, id=my_id)
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)

def product_detail_view(request, my_id):
    obj = Product.objects.get(id=my_id)
    context = {
        'object': obj
        # alternatively - setting manually all parameters;
        # 'title': obj.title,
        # 'summary': obj.summary,
        # 'price': obj.price
        #  etc.
    }
    return render(request, 'products/product_detail.html', context)


def product_create_view(request):
    initial_data = {
        'title': "Put your title here",
        'price': "Just name your price"
    }
    obj = Product.objects.get(id=1)
    # next part is actually everything that was the   original version 1st product_create_view
    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)

# # 1st version - using the build of Product Form with MetaClass
# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm
#     context = {
#         'form': form
#     }
#     return render(request, 'products/product_create.html', context)


# using build of RawProductForm version
# purpose? is it more safe? definitely that demands fullfilling all fields by user
# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#     if my_form.is_valid():
#         # now as data is right - test
#         print(my_form.cleaned_data)
#         Product.objects.create(**my_form.cleaned_data)
#         my_form = RawProductForm()
#         # you can add
#         # else:
#         #     print(my_form.errors)
#     context = {
#         'form': my_form
#     }
#     return render(request, 'products/product_create.html', context)




