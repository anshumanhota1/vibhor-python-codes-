from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.

def post_view(request):
    posts = Post.objects.all()
    return render(request,'posts/index.html', {"posts": posts})


def post_create(request):
    return HttpResponse("<h2>Create</h2>")


def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request,'posts/details.html', {"post": post})


def post_update(request):
    return HttpResponse("<h2>Update</h2>")

    
def post_delete(request):
    return HttpResponse("<h2>Delete</h2>")