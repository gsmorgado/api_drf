from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from api.models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post,
       # fields = '__all__'
        exclude = ['is_removed', 'created', 'modified']