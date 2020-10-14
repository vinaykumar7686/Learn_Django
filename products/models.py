from django.db import models
# Create your models here.
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Products(models.Model):

    user = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
    name = models.CharField(max_length = 20)
    content = models.TextField(null = True, blank = True)
    price = models.DecimalField(default=0.00, max_digits = 10, decimal_places = 2)
    inventory = models.IntegerField(default = 0)
    featured = models.BooleanField(default = False)

    def __str__(self):
        return self.name

    def has_inventory(self):
        return self.inventory>0