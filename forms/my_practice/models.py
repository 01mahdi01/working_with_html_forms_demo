from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class newuser(AbstractUser):
    pass

class products(models.Model):
    name = models.CharField(max_length=60)
    emount = models.IntegerField()
    price = models.IntegerField()
    # def __str__(self):
    #     return f"{self.name},price:{self. price}$"


class vote(models.Model):
    count = models.IntegerField(default=0)
    user = models.ForeignKey(newuser, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
