from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    cooked_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self) -> str:
        return self.name 
    
class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ingredients = models.ManyToManyField(Product, through='RecipeProduct')

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self) -> str:
        return self.name 

class RecipeProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    weight = models.IntegerField()

    class Meta:
        unique_together = ('recipe', 'product')
        verbose_name = "Добавить в рецепт"
        verbose_name_plural = "Добавить в рецепт"

    def __str__(self) -> str:
        return f"{self.recipe.name}_{self.product.name}"