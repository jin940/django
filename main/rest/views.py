from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination

from .serializers import PostSerializer

from .models import Post

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/post-list',
        'Detail Post' : '/post-detail/<str:pk>',
        'Create' : '/post-create',
        'Update' : '/post-update/<str:pk>/',
        'Delete' : '/post-delete/<str:pk>/',
    }
    return Response(api_urls)

# return one Post
@api_view(['GET'])
def postDetail(request, pk):
    post = Post.objects.get(id = pk)
    serializer = PostSerializer(post, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def postCreate(request):
    serializer = PostSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def postUpdate(request, pk):
    post = Post.objects.get(id = pk)
    serializer = PostSerializer(instance=post, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

class ApiDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ApiListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
