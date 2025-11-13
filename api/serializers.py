from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("id", "created_at", "user")