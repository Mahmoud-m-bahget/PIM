from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.Product_OverView , name = "Product-overView"),
    path('list-product', views.Lsit_Product , name = "lsit-Product"),
    path('product-detail/<str:pk>', views.Product_Detail , name = "product-detail"),
    path('create-product', views.Create_Product , name = "create-product"),
    path('create-multiple-product', views.Create_Multiple_Product , name = "create-multiple-product"),
    path('update-product/<str:pk>', views.Update_Product , name = "update-product"),
    path('delete-product/<str:pk>', views.Delete_Product , name = "delete-product"),
]

