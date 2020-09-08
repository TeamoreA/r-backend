from rest_framework import serializers
from apps.products.models import Category
from apps.products.models import Product

class CategorySerializer(serializers.ModelSerializer):
    """
    serializer for the Category model
    """
    class Meta:
        model = Category
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model
    """
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("owner", "Created_at", "updated_at")

    def create(self, validated_data):
        """add owner as the current user during creation"""
        validated_data.update(
            {'owner': self.context['request'].user}
        )
        product = Product.objects.create(**validated_data)
        return product