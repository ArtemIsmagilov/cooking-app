from django.urls import  path
from rest_framework.urlpatterns import format_suffix_patterns

from foods.views import (
    AddProductToRecipe,
    CookRecipe,
    ShowRecipesWithoutProduct,
)

urlpatterns = [
    path('add_product_to_recipe/', AddProductToRecipe.as_view()),
    path('cook_recipe/', CookRecipe.as_view()),
    path('show_recipes_without_product/<int:product_id>/', ShowRecipesWithoutProduct.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
