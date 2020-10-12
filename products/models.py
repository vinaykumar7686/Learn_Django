from django.db import models
# Create your models here.
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Products(models.Model):

    user = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
    name = models.CharField(max_length = 20)
    content = models.TextField(null = True, blank = True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

