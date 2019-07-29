from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewPost
from .models import Post
# Create your views here.

def reviews(request):
    reviews = Post.objects
    return render(request, 'reviews.html', {'reviews':reviews})

def my_reviews(request):
    if request.method == 'POST':
        form = ReviewPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post/' + str(form.id))
    else:
        form = ReviewPost()
        return render(request, 'new.html', {'form':form})


def create(request):
    post = Post()
    post.image = request.GET['image']
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.save()
    return redirect('/post/' + str(post.id))
    
# def newpost(request):
#     return render(request, 'new.html', {'form':form})
#     pass
