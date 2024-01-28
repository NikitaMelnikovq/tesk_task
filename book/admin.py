from django.contrib import admin
from .models import Product, Recipe, RecipeProduct

class RecipeIngredientInline(admin.StackedInline):
    model = Recipe
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]


admin.site.register(Product)
admin.site.register(Recipe)
admin.site.register(RecipeProduct)
