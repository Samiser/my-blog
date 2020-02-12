from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from .models import Post

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
    
def home_view(request):
    try:
        post = Post.published.order_by("-publish")[0]
    except:
        post = 0
    return render(request, 'blog/index.html', {'post':post})

class AboutView(TemplateView):
    template_name = 'blog/about.html'

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, 
                                    status='published', 
                                    publish__year=year, 
                                    publish__month=month,
                                    publish__day=day)

    return render(request, 'blog/post/detail.html', {'post':post})
