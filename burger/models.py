from django.db import models
from account.models import User,CustomerDtail

# Create your models here.


class Ingredient(models.Model):
    salad = models.IntegerField(default=0)
    cheese = models.IntegerField(default=0)
    meat =models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'salad:{self.salad} ,cheese:{self.cheese}, meat:{self.meat}'
    



class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ingredients = models.OneToOneField(Ingredient, on_delete=models.CASCADE)
    customer =models.OneToOneField(CustomerDtail, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    orderTime = models.DateTimeField(auto_now_add=True)
    payment =models.BooleanField(default=False,blank=True,null=True)

    def __str__(self) -> str:
        return f"order:{self.user.email}"




