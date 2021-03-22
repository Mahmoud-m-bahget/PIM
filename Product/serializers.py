from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
   # product_count = serializers.SerializerMethodField(read_only=True)

   
    class Meta:
        model = Products 
        fields =  '__all__'
   

    #def get_product_count(self,obj):
    #   return obj.category.count()