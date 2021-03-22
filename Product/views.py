from django.shortcuts import render , get_object_or_404
from .models import Products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from .serializers import  ProductsSerializer


# product sections

'''
showing all product urls
'''
@api_view(["GET"])
def Product_OverView(request):
    Product_urls = {
        "List Product"   : "list-product",
        "Product Detail" : "product-detail/<str:pk>",
        "Create Product" :"create-product",
        "Create multiple Product" : "create-multiple-product",
        "Update Product" :"update-product/<str:pk>",
        "Delete Product" :"delete-product/<str:pk>",
    }
    return Response(Product_urls)


'''
Function to show all active product
'''
@api_view(["GET"])
def Lsit_Product(request):
    product = Products.objects.filter(State="Active").order_by('-id')
    serializer = ProductsSerializer(product , many = True)
    return Response(serializer.data)


'''
Function to show product detail and teak id as a primary key
'''
@api_view(["GET"])
def Product_Detail(request , pk):
    try:
        product = Products.objects.get(id = pk)
        serializer = ProductsSerializer(product , many = False)
        return Response(serializer.data) 
    except:
        its_not_valid = "Not found"
        return Response(its_not_valid)
    
'''
Function to create product
'''
@api_view(["POST"])
def Create_Product(request):
    serializer = ProductsSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    not_valid = "Data not valid "
    return Response(not_valid)




'''
Function to multiple create product takes only multiple data
'''
@api_view(["POST"])
def Create_Multiple_Product(request):
    serializer = ProductsSerializer(data = request.data , many = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    not_valid = "Data not valid "
    return Response(not_valid)



'''
Function to update product and teak id as primary key
'''
@api_view(["PATCH"])
def Update_Product(request , pk):
    product = Products.objects.get(id = pk)
    serializer = ProductsSerializer(instance = product ,data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    not_valid = "Data not valid "
    return Response(not_valid)


'''
Function to delete product and teak id as primary key
'''
@api_view(["DELETE"])
def Delete_Product(request , pk):
    try:
        product = Products.objects.get(id = pk)
        product.delete()
        return Response("Items deleted")
        
    except:
        its_not_valid = "Not found"
        return Response(its_not_valid)