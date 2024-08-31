from django import forms
from .models import Order

class OrderBuyeUpdate(forms.ModelForm):
    class Meta:
        model = Order
        fields =['payment']