from django.db import models

# Create your models here.
class Client(models.Model):

    #Fields for Client information
    name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    DL = models.CharField(max_length=9)

    def __str__(self):
        return self.name
