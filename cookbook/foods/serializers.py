from rest_framework import serializers

from .models import (
    Recipe,
    RecipeProduct,
)


class RecipeSerializer(serializers.Serializer):
    recipe_id = serializers.IntegerField()
    title = serializers.CharField()


class RecipeIdSerializer(serializers.Serializer):
    recipe_id = serializers.IntegerField()


class RecipeProductSerializer(serializers.Serializer):
    weight = serializers.IntegerField()
    recipe_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
