from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.Category_OverView , name = "category-overview"),
    path('list-category', views.List_Category , name = "list-category"),
    path('category-id/<str:pk>', views.number_of_product , name = "category-id"),
    path('category-detail/<str:pk>', views.Category_Detail , name = "category-detail"),
    path('create-category', views.Create_Category , name = "create-category"),
    path('update-category/<str:pk>', views.Update_Category , name = "category-update"),
    path('delete-category/<str:pk>', views.Delete_Category , name = "delete-category"),
]
