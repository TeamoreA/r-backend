from rest_framework import serializers

from apps.products.models import Category, Image, Product


class CategorySerializer(serializers.ModelSerializer):
    """
    serializer for the Category model
    """

    class Meta:
        model = Category
        fields = ["id", "name"]


class ImageSerializer(serializers.ModelSerializer):
    """
    serializer for the Image model
    """

    class Meta:
        model = Image
        fields = ["image"]


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model
    """

    images = serializers.SerializerMethodField()
    product_images = serializers.ListField(
        child=serializers.ImageField(max_length=100000, allow_empty_file=False)
    )

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("owner", "Created_at", "updated_at")

    def get_images(self, obj):
        images = Image.objects.filter(product=obj)
        serializer = ImageSerializer(images, many=True, context=self.context)
        return serializer.data

    def create(self, validated_data):
        """add owner as the current user during creation"""
        validated_data.update({"owner": self.context["request"].user})
        image = validated_data.pop("product_images")
        product = Product.objects.create(**validated_data)
        for img in image:
            data = {"product": product, "image": img}
            Image.objects.create(**data)
        return product
