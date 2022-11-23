from django.db import models

# Create your models here.
class Math(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    summary = models.TextField()
    featured = models.BooleanField(null=True) #null true or default=true means make the first fields contain this without values
