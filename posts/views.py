from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def post_view(request):
    posts = Post.objects.all()
    return render(request,'posts/index.html', {"posts": posts})


def post_create(request):
    return HttpResponse("<h2>Create</h2>")


def post_details(request):
    return HttpResponse("<h2>Details</h2>")


def post_update(request):
    return HttpResponse("<h2>Update</h2>")

    
def post_delete(request):
    return HttpResponse("<h2>Delete</h2>")