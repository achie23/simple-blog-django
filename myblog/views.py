from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.
def index(request):
    model = Post
    template_name = "posts.html"
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

class PostView(generic.DetailView):
    model = Post
    template_name = "posts.html"
    
    def post(request, pk):
        posts = Post.objects.get(id=pk)
        return render(request, 'posts.html', {'posts': posts})