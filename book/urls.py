from django.urls import path
from .views import show_recipes_without_product 
urlpatterns = [
    path("<int:product_id>", show_recipes_without_product, name="home")
]


app_name = "book"
