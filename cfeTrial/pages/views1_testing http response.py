from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, )
    print(request.user)
    #return HttpResponse("<h1>Hello World</h>")
    return render(request, 'product/home.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'product/contact.html', {})
    
def about_view(request, *args, **kwargs):
    return render(request, 'product/about.html', {})



#using django to request a html use render not httpresponse