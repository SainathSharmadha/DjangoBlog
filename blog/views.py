from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if(form.is_valid()):
            post = form.save(commit=False)
            post.user = request.POST['user']
            post.comment = request.POST['comment']
            print (request.POST)
            post.save()

    comment_form = PostForm()
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html',{'posts':posts,'comment_form':comment_form })







