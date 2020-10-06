from django.db import models

# Create your models here.

class Profiles(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField(null = False, blank = False)
    content = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.name
