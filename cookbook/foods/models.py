from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200, unique=True)
    used = models.PositiveIntegerField()

    def __str__(self):
        return f'Product(pk={self.pk!r} title={self.title!r} used={self.used!r})'


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)

    products = models.ManyToManyField(Product, through="RecipeProduct", through_fields=("recipe", "product"))

    def __str__(self):
        return f'Recipe(pk={self.pk!r} title={self.title!r})'


class RecipeProduct(models.Model):
    weight = models.PositiveIntegerField()

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['recipe', 'product'], name='unique_product'),
        ]

    def __str__(self):
        return f'RecipeProduct(pk={self.pk!r} weight={self.weight!r})'
