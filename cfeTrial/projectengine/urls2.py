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
from django.urls import path

#my imports
# from pages import views === this will have been the path  path('', views.home_view, name=)
from pages.views import home_view, contact_view, about_view
from productProvingStubborn.views import (
        delete_view,
        get_all_view,
        delete_view,
        dynamic_lookup_view, 
        modified_view, 
        create_render_initial_data, 
        product_detail_view, 
        product_create_view,
        product_create_raw_form_view,
         product_create_pure_django_form,
        product_create_pure_django_form_w_properties, 
        product_create_overide_model_form_with_pure_django_form
)

urlpatterns = [

    path('p/<int:id>', product_detail_view, name="product-details"),
    path("create/", product_create_view, name="create"),
    path("createb/", product_create_raw_form_view, name="create2"),
    path("createc/", product_create_pure_django_form, name="create3"), 
    path("created/", product_create_pure_django_form_w_properties, name='create4'),
    path("createe/", product_create_overide_model_form_with_pure_django_form, name='create5'),
    path("createf/", create_render_initial_data, name="create6"),
    path("modify/<int:id>", modified_view, name='modify-product'),
    # path("product/<int:id>", dynamic_lookup_view, name="create8"),
    path ("product/<int:id>/delete/",  delete_view, name="delete-product"),
    path ("", get_all_view, name="list_items"),


    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),


    path('admin/', admin.site.urls),
]


#import views directly from the apps file to urls.py root
#here we are using the first kind. if you import it from the pages you call 
#it will views.name 