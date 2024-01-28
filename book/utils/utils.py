from django.shortcuts import get_object_or_404
from book.models import Recipe, Product, RecipeProduct

def add_product_to_recipe(recipe_id, product_id, weight):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        product = get_object_or_404(Product, id=product_id)

        recipe_ingredient, created = RecipeProduct.objects.get_or_create(recipe=recipe, product=product)
        recipe_ingredient.weight_in_grams = weight
        recipe_ingredient.save()

def cook_recipe(recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients = recipe.ingredients.all()

    for ingredient in ingredients:
        product = ingredient.product
        product.times_used += 1
        product.save()
