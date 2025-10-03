from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Post
from django.views.generic import ListView

# Create your views here.
class BlogPageView(TemplateView):
    template_name = "blog_template.html"
    def get(self, request , slug):
        try:
            self.post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            return render(request, "_404.html")

        return render(request, self.template_name , {"post": self.post})
    
class BlogListView(ListView):
    template_name = "blog_list.html"
    paginate_by = 5
    model = Post
    context_object_name = 'posts'
    ordering = ['-created_at']

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(title__icontains=query)
        return qs.order_by('-created_at')

class BlogSearchView(ListView):
    template_name = "blog_list.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Post.objects.filter(title__icontains=query)
        return Post.objects.all().order_by('-created_at')