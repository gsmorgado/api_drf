from codecs import raw_unicode_escape_decode
import imp
from turtle import pos
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PostSerializers, serializers
from .models import Post

from django.http import Http404


class Post_APIView(APIView):
    
    def get(self, request, format=None, *args, **kwargs):
        post= Post.objects.all()
        serializers= PostSerializers(post, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers=PostSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class Post_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(selt, request,pk,format=None):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializers = PostSerializers(post)
        return Response(serializers.data)
    
    def put(self, request, pk, format=None):
        post= self.get_object(pk)
        serializers= PostSerializers(post, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        post= self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
