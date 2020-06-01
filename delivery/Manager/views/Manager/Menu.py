from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from .serializer import AuthorSerializer, FriendSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.renderers import JSONRenderer
import uuid

class Menu(APIView):
    def get(self, request, post_id, **kwargs):
        try:
            current_user_profile = request.user.author
            post = get_object_or_404(Post, pk = post_id)
        except:
            return HttpResponse(status=404)
        new_comment = Comment.objects.create(post_id=post, author=current_user_profile)
        request.session["Comment_id"] = str(new_comment.id)
        serializer = CommentSerializer(new_comment)
        return Response({"serializer": serializer})

    def post(self, request, post_id, **kwargs):

        post = get_object_or_404(Post, pk = post_id)
        try:
            id = uuid.UUID(request.session['Comment_id']).hex
            new_comment = Comment.objects.get(id=id)
        except:
            new_comment = Comment.objects.create(post_id = post, author=request.user.author)
        serializer = CommentSerializer(new_comment, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("get_one_post", post.id)

        print("awsl")
        print(serializer.errors)
        return Response({'serializer': serializer})

class Dish(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Dish.objects.get(pk=pk)
        except Dish.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
