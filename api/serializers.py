from rest_framework import serializers
from .models import User, Craftsman, Apprentice, Category, Order, Job


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'is_craftsman', 'is_apprentice']

    def validate(self, data):
        if 'username' in data and User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username already exists.")
        if 'email' in data and User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email already exists.")
        return data


class CraftsmanSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User .objects.all())
    photo = serializers.ImageField(required=False)

    class Meta:
        model = Craftsman
        fields = ['id', 'user', 'surname', 'telephone', 'address', 'skills', 'photo']


class ApprenticeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User .objects.all())
    selfie = serializers.ImageField(required=False)

    class Meta:
        model = Apprentice
        fields = ['id', 'user', 'skill_to_learn', 'selfie', 'category']


class CategorySerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'photo']


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User .objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'user', 'category', 'description', 'status']


class JobSerializer(serializers.ModelSerializer):
    craftsman = serializers.PrimaryKeyRelatedField(queryset=Craftsman.objects.all())
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())

    class Meta:
        model = Job
        fields = ['id', 'craftsman', 'order', 'status']