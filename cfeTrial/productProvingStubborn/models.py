from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    summary = models.TextField()
    featured = models.BooleanField(null=True) #null true or default=true means make the first fields contain this without values

#since changing our url from say product/<int:id>
#to say                          p/<int:id>
# you will have to go and change every position you used the product

    def get_absolute_url(self):
        # return f"products/{self.id}/"  ###you will have to go about changing every link that starts with product to say item.get_absolute_url
        return reverse("productProvingStubborn:product-details", kwargs={"id": self.id}) #here you use the name in the url.py names to any particular link just incase it got changed
                                                             # testing it on product-details so as to become dynamice
                                                             #we append our app name infront of the url name we choose to change

    