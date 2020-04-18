from rest_framework import serializers
from .models import BinaryTree


class BinaryTreeSerializer(serializers.ModelSerializer):
    # Serializer of Model Binary Tree
    class Meta:
        model = BinaryTree
        fields = '__all__'
