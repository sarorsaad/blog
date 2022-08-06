from pdb import post_mortem
from urllib import request
from django.shortcuts import render

from .models import Posts

# Create your views here.
def all_posts (request):
    posts=Posts.objects.all()
    return render(request,'post.html',{'mah':posts})
