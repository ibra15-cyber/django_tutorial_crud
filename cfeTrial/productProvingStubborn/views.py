from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import (
    ProductForm, 
    RawProductForm, 
    RawProductFormWith_properties, 
    ProductFormOveride
)

# Create your views here.
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        "form" : form
    }
    return render(request, 'products/create.html', context)


# WITHOUT A DB saving to terminal from raw form
def product_create_raw_form_view(request):
    print(request.GET)
    print(request.POST) #Gives you the title
    if request.method == "POST":
        my_title = request.POST.get('title')
        print("Want it to print the title: " , my_title)
    #to save in databe 
    # Product.objects.create(title=my_title) ##this alone will ask for price because that field can't be empty
    ##so when you are using django to render a form you pass it in context
    ##but if we use raw form, we just grate the input names back in the view and map them 
    ##to variables in our view
    ##so in the case of our assignment; the ladies could have completed it; we will grab their html 
    ##and then call their variables and map them to db
    context = {
    }
    return render(request, 'products/create_with_raw_form.html', context)


def product_create_pure_django_form(request):
    form = RawProductForm(request.GET)

    #getting a reply from the form that uses pure django form without using the form model
    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            print(form) ##or form.cleaned_data will format it
            #now we can pass whats coming back from the form to our databas
            Product.objects.create(**form.cleaned_data)
            # RawProductForm(request.GET)
        else: 
            print(form.errors)

    context = {
        'form': form
    }

    return render(request, 'products/create_with_pure_djangoF.html', context)



def product_create_pure_django_form_w_properties(request):
    form = RawProductFormWith_properties()
    if request.method == "POST":
        form = RawProductFormWith_properties(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
    context = {
        'form': form
    }
    return render(request, 'products/create_with_pure_django_Form_properies.html', context)

def product_create_overide_model_form_with_pure_django_form(request):
   template_name = 'products/create_overide_djF_with_MdF.html'
   form = ProductFormOveride()
   context = {
    'form': form
   }
   if request.method == 'GET' :
       form = ProductFormOveride()
   if request.method == 'POST' :
        form = ProductFormOveride(request.POST or None)
        if form.is_valid():
            form.save() #enough when using model form; otherwise useform.cleaned_data
       
   return render(request,template_name,context)

def create_render_initial_data(request):

    initial_data = {
       'title': "my new title",
       'price': 898
    }

    form = ProductFormOveride(initial=initial_data)
    context = {
            'form': form
        }
    template_name = 'products/create_render_initial_data.html'

    

    if request.method == 'GET' :
       form = ProductFormOveride()
    if request.method == 'POST' :
        form = ProductFormOveride(request.POST or None, )
        if form.is_valid():
            form.save() #enough when using model form; otherwise useform.cleaned_data
    return render(request,template_name,context)

#modified it from just getting item with id 50 to id
# to handle error; instead of using get use 404_get
def modified_view(request, id):
    template_name = 'products/modify.html'
#    obj = Product.objects.get(id=50)
    # obj = Product.objects.get(id=id) #get object from db 
    obj = get_object_or_404(Product, id=id)
    form = ProductFormOveride(request.POST or None, instance=obj)
    context = {
        'form': form
    }
    if request.method == 'GET' :
       
       pass
    if request.method == 'POST' :
        form = ProductFormOveride(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            print(obj.id)
            print(type(obj.id))
            return redirect("../../../product/" + str(obj.id))
    return render(request,template_name,context)


#in pure form, you do not need to pass a form, therefore no context, 
#you rather map the items from db to the varibles names that you will use in the input fields


# def delete_view(request, id):
#     # template_name = 'products/delete.html'
#     # obj = Product.objects.get(id=id)
#     obj = get_object_or_404(Product, id=id)
#     if request.method == "POST":
#         obj.delete()
#     context : {
#         'object' : obj
#     }
#     # title : obj.title
#     # my_id : obj.id
#     # if request.method == "POST" or None:
#     #     # obj = get_object_or_404(Product, id=id)

#     #     my_id : obj.id
        
#     #     obj.delete()
#     #     #return redirect("../../../") #go back to the root folder
#     # redirect("../../../")
#     return render(request,'products/delete.html', context)
def delete_view(request, id):
    template_name = "products/delete.html"
    obj = get_object_or_404(Product, id=id) #get obj by id
    if request.method == "POST":
        obj.delete() ####default delete fn
        return redirect('../../../') #go back to products page where the items will be listed
    context = {
		'object' : obj	                     
	}
    return render(request, template_name, context)


def product_detail_view(request, id):
    obj = Product.objects.get(id=id)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }

#instead taking what you want from the db here; just pass everything and catch what you need in the template
    context = {
        "object" : obj
    }
    return render(request, 'products/detail.html', context)


def get_all_view(request):
    queryset = Product.objects.all()
    # form = ProductFormOveride()
    context = {
        'obj': queryset
    }
    return render(request, 'products/list_all.html', context)

def dynamic_lookup_view(request, id):
   template_name = 'products/dynamic_lookup.html'
   obj = Product.objects.get(id=id)
#    form = ProductFormOveride()
   context = {
    'obj': obj
   }
   if request.method == 'GET' :
       
       pass
   if request.method == 'POST' :
       pass
   return render(request,template_name,context)
