from rest_framework import serializers
from .models import Order, Ingredient
from account.models import CustomerDtail

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDtail
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        customer_data = validated_data.pop('customer')

        ingredients = Ingredient.objects.create(**ingredients_data)
        customer = CustomerDtail.objects.create(**customer_data)

        order = Order.objects.create(
            user=validated_data['user'],
            ingredients=ingredients,
            customer=customer,
            price=validated_data['price'],
        )

        return order
