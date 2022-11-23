"""projectengine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#my imports
# from pages import views === this will have been the path  path('', views.home_view, name=)
from pages.views import home_view, contact_view, about_view

urlpatterns = [

#    path("", include('productProvingStubborn.urls')),
    path("product/", include('productProvingStubborn.urls')), #changed product to p and it still worked because we handled that with absolute url
    #better call it product here and remove it in the main product folder ot make it distinct incase we got lots app in our pro

    #paths from a diff app called pages
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),


    path('admin/', admin.site.urls),
]


#import views directly from the apps file to urls.py root
#here we are using the first kind. if you import it from the pages you call 
#it will views.name 