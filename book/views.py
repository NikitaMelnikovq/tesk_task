from django.http import JsonResponse
from .models import Product, Recipe, RecipeProduct
from django.shortcuts import render
from django.db.models import Sum, F

def home(request):
    return render(request, "book/table.html")

def show_recipes_without_product(request, product_id):
    product_id = request.GET.get('product_id')

    recipes_without_product = Recipe.objects.exclude(recipeingredient__product_id=product_id).annotate(
        total_weight=Sum('recipeingredient__weight_in_grams'))

    recipes_with_less_than_10g = recipes_without_product.filter(total_weight__lt=10)

    return render(request, 'recipes_without_product.html', {'recipes': recipes_with_less_than_10g})
