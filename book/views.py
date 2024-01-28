from django.http import JsonResponse
from .models import Product, Recipe, RecipeProduct
from django.shortcuts import render
from django.db.models import Sum, F

def show_recipes_without_product(request, product_id):
    recipes_without_product = Recipe.objects.exclude(recipeproduct__product_id=product_id).annotate(
        total_weight=Sum('recipeproduct__weight'))

    recipes_with_less_than_10g = recipes_without_product.filter(total_weight__lt=10)

    result = recipes_with_less_than_10g.union(recipes_without_product)
    
    return render(request, 'book/table.html', {'recipes': result})