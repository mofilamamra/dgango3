from django.shortcuts import render 
from django.forms.models import model_to_dict
from .models import Post

# Create your views here.


def postlist(request):

    post_list = Post.objects.all()

    return render (request , 'post-list.html' ,{'post_list':post_list,})


def postdetail(request ,id ):
    
    post_detail = Post.objects.get(id=id)

    return render (request , 'post-detail.html' ,{'post_detail':post_detail,})    