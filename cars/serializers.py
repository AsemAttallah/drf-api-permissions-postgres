from rest_framework import serializers
from .models import Car,Post

class CarSerializer(serializers.ModelSerializer):
    class Meta :
        model = Car
        # fields = ['purchaser','type','desc']
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta :
        model = Post
        fields='__all__'