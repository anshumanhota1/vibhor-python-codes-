from urllib.parse import quote_plus
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from .models import Post
from .forms import PostForm
from django.db.models import Q

# Create your views here.

def post_view(request):
    
    post_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(user__first_name__icontains=query)|
            Q(user__last_name__icontains=query)
        ).distinct()
    paginator = Paginator(post_list, 2) # Show 25 posts per page
    page_var = 'page'
    page = request.GET.get(page_var)
    posts = paginator.get_page(page)
    return render(request,'posts/index.html', {"posts": posts, 'page_var': page_var})


def post_create(request):
    if not request.user.is_staff and not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    """
        create a instance of  PostFrom class from the forms module
        for validtions pass the request.Post argument
        pass 'or None' so that the validation are given when 
        invaild data is being passed and not always(vid ref 20 try dango 1.9)
    """
    if form.is_valid and request.method == "POST":
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        #create a post and save it in database
        messages.success(request, "Post created successfully")
        return redirect(post.get_absolute_url())

    return render(request,'posts/post_form.html', {"form": form})


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    share_string = quote_plus(post.content)
    return render(request,'posts/details.html', {"post": post, 'share_string': share_string })


def post_update(request, slug):
    if not request.user.is_staff and not request.user.is_superuser:
        raise Http404
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
    if not request.user.is_staff and not request.user.is_superuser:
        raise Http404
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, "Post deleted successfully")
    return redirect("posts:home")


"""
the future publishing of post and the drafting of the post functions have not
been added, if you want to refer those please 
ref vid 34, 35, & 36 from try django 1.9 
"""