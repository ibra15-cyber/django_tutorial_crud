from django.urls import path

#my imports
# from pages import views === this will have been the path  path('', views.home_view, name=)
from .views import (
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

#to make sure dynamic routing works add the app_name here
# then go to the abosolue path and append the app name intront of the url name that you decide to change
app_name = "productProvingStubborn"
urlpatterns = [
    # in a particular program it is good to make all the url start with the app name so here product
    path ("", get_all_view, name="list_items"),
    path('/<int:id>', product_detail_view, name="product-details"),
    path("create/", product_create_view, name="create"),
    path("createb/", product_create_raw_form_view, name="create2"),
    path("createc/", product_create_pure_django_form, name="create3"), 
    path("created/", product_create_pure_django_form_w_properties, name='create4'),
    path("createe/", product_create_overide_model_form_with_pure_django_form, name='create5'),
    path("createf/", create_render_initial_data, name="create6"),
    path("modify/<int:id>", modified_view, name='modify-product'),
    # path("product/<int:id>", dynamic_lookup_view, name="create8"),
    path ("/<int:id>/delete/",  delete_view, name="delete-product"),
    
]


#import views directly from the apps file to urls.py root
#here we are using the first kind. if you import it from the pages you call 
#it will views.name 