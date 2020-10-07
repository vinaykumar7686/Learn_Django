from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length = 25)
    fback = models.TextField()
    rating = models.IntegerField(default = 5)

    def __str__(self):
        return self.name+" :"+str(self.rating)

