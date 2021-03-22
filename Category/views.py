from django.shortcuts import render
from .models import Categories
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import  CategoriesSerializer
from Product.models import Products
#from Product.serializers import ProductsSerializer

'''
Showing all category urls
'''
@api_view(["GET"])
def Category_OverView(request):
    Category_urls = {
        "List Category": "list-category",
        "Category Detail" : "category-detail/<str:pk>",
        "Create Category":"create-category",
        "Update Category":"update-category/<str:pk>",
        "Delete Category":"delete_category/<str:pk>",
        "Number of product": "category-id/<str:pk>"
    }
    return Response(Category_urls)



'''
Function to show all category
'''
@api_view(["GET"])
def List_Category(request):
    category = Categories.objects.all().order_by("-id")
    serializer = CategoriesSerializer(category , many = True)
    return Response(serializer.data)



'''
function to get number of product in category it teaks category id 
'''
@api_view(["GET"])
def number_of_product(request, pk):
    if Categories.objects.filter(id = pk).exists():
        products = Products.objects.filter(category__id=pk)
        pro_number = products.count()
        if pro_number == 0:
            catgory_product_number = {
                "Category id" : pk,
                "Category product number": 0
            }
            return Response(catgory_product_number)
        catgory_product_number = {
                "Category id" : pk,
                "Category product number": pro_number
            }
        return Response(catgory_product_number)

    its_not_valid = "data not found"
    return Response(its_not_valid)

'''
Function to show category detail and teak id as a primary key
'''

@api_view(["GET"])
def Category_Detail(request , pk):
    try:
        category = Categories.objects.get(id = pk)
        serializer = CategoriesSerializer(category , many = False)
        return Response(serializer.data)
    except:
        its_not_valid = "Not found"
        return Response(its_not_valid)



'''
Function to create category
'''

@api_view(["POST"])
def Create_Category(request):
    serializer = CategoriesSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    not_valid = "Data not valid "
    return Response(not_valid)


'''
Function to update category and teak id as primary key
'''

@api_view(["PATCH"])
def Update_Category(request , pk):
    category = Categories.objects.get(id = pk)
    serializer = CategoriesSerializer(instance = category ,data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    not_valid = "Data not valid "
    return Response(not_valid)




'''
Function to delete category and teak id as primary key
'''

@api_view(["DELETE"])
def Delete_Category(request , pk):
    try:
        category = Categories.objects.get(id = pk)
        category.delete()
        return Response("Items deleted")
    except:
        its_not_valid = "Not found"
        return Response(its_not_valid)