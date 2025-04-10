from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True, default= None)
    phone = models.BigIntegerField(null=True, blank=True, default=None)
    message = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
