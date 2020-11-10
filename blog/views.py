from django.shortcuts import render,redirect,reverse 
from django.forms.models import model_to_dict
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):

    post_list = Post.objects.all()

    return render (request , 'blog/post-list.html' ,{'post_list':post_list,})

def post_detail(request,id):
    post = Post.objects.get(id=id)
    return render(request,'blog/post_detail.html',{'signal_post':post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:post_list'))
    else :
        form = PostForm()
    return render(request,'blog/post_create.html',{'form' : form})

def post_edit(request,id):  
    post = Post.objects.get(id=id)    
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:post_detail',kwargs={'id': post.id}))
    else :
            form = PostForm(instance=post)
    return render(request,'blog/post_edit.html',{'form' : form})
         