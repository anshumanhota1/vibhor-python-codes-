from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.

def post_view(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 2) # Show 25 posts per page
    page_var = 'page'
    page = request.GET.get(page_var)
    posts = paginator.get_page(page)
    return render(request,'posts/index.html', {"posts": posts, 'page_var': page_var})


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    """
        create a instance of  PostFrom class from the forms module
        for validtions pass the request.Post argument
        pass 'or None' so that the validation are given when 
        invaild data is being passed and not always(vid ref 20 try dango 1.9)
    """
    if form.is_valid and request.method == "POST":
        post = form.save(commit=False)
        post.save()
        #create a post and save it in database
        messages.success(request, "Post created successfully")
        return redirect(post.get_absolute_url())

    return render(request,'posts/post_form.html', {"form": form})


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request,'posts/details.html', {"post": post})


def post_update(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid and request.method == "POST":
        post = form.save(commit=False)
        post.save()
        messages.success(request, "Post updated successfully")
        return redirect(post.get_absolute_url())
    else:
        messages.error(request, "Post not updated successfully")
    context = {
        "title": post.title,
        "post": post,
        "form": form
    }
    return render(request,'posts/post_form.html', context)

    
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, "Post deleted successfully")
    return redirect("posts:home")


