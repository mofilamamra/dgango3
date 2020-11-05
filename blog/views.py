from django.shortcuts import render 
from django.forms.models import model_to_dict
from .models import Post

# Create your views here.


def post_list(request):

    post_list = Post.objects.all()

    return render (request , 'blog/post-list.html' ,{'post_list':post_list,})
def post_detail(request,id):
    post = Post.objects.get(id=id)
    return render(request,'blog/post_detail.html',{'signal_post':post})