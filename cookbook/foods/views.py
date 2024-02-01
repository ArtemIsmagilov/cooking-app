from rest_framework import (
    status,
    views,
)
from rest_framework.request import Request
from rest_framework.response import Response
from django.db import IntegrityError
from django.db.models import (
    F,
    Subquery,
)
from django.shortcuts import render

from .serializers import (
    RecipeProductSerializer,
    RecipeIdSerializer,
    RecipeSerializer,
)
from .models import (
    RecipeProduct,
    Product,
)


class AddProductToRecipe(views.APIView):

    def post(self, request: Request, format=None) -> Response:
        serializer = RecipeProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            form_data = serializer.validated_data
            weight, product_id, recipe_id = form_data['weight'], form_data['product_id'], form_data['recipe_id']
            try:

                RecipeProduct.objects.update_or_create(
                    recipe_id=recipe_id,
                    product_id=product_id,
                    defaults={"weight": weight},
                    create_defaults=form_data,
                )

                return Response(serializer.data, status=status.HTTP_200_OK)
            except IntegrityError:
                return Response({'detail': 'Not found Recipe or Product'}, status=status.HTTP_400_BAD_REQUEST)


class CookRecipe(views.APIView):

    def put(self, request: Request, format=None) -> Response:
        serializer = RecipeIdSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            recipe_id = serializer.validated_data['recipe_id']

            subquery = Subquery(
                RecipeProduct.objects
                .filter(recipe_id=recipe_id)
                .values('product_id')
            )
            Product.objects.filter(pk__in=subquery).update(used=F('used') + 1)

            return Response(serializer.data, status=status.HTTP_200_OK)


class ShowRecipesWithoutProduct(views.APIView):

    def get(self, request: Request, product_id: int, format=None) -> Response:
        recipes = RecipeProduct.objects.raw("""
             SELECT foods_recipeproduct.id, foods_recipeproduct.recipe_id, foods_recipe.title
             FROM foods_recipeproduct
             INNER JOIN foods_recipe ON foods_recipeproduct.id=foods_recipe.id
             WHERE NOT(foods_recipeproduct.product_id=%s) OR foods_recipeproduct.weight < 10
             GROUP BY recipe_id;
             """, (product_id,))

        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def index(request: Request) -> Response:
    return render(request, 'foods/index.html')
