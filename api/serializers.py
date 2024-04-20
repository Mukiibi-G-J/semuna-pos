from rest_framework import serializers
from product.models import Products



class ProductsSerializers(serializers.ModelSerializer):
    price = serializers.FloatField(source='cost')
    cost_price = serializers.FloatField(source='unit_price')
    class Meta:
        model = Products
        fields = '__all__'
    
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['price'] = data.pop('cost')
        data['cost_price'] = data.pop('unit_price')
        return data