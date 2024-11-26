from rest_framework import serializers
from .models import Restaurant, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'rating',
            'comment'
        ]

class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            "name",
            "cuisine",
            "city",
        ]

class RestaurantDetailSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = [
            "name",
            "rating",
            "review_count",
            "price",
            "cuisine",
            "image",
            "address",
            "city",
            "zip_code",
            "state",
            "phone",
            "review_set",
        ]