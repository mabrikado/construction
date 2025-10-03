from django.shortcuts import render , HttpResponse
from django.views.generic import TemplateView
from blog.models import Post
from django.views import View

# Create your views here.


class HomeView(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_at')[:3]
        return render(request, self.template_name, {"posts": posts})

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_at')[:3]

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Log the submission (or send an email in production)
        print(f"Contact Form Submission:\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}")

        context = {
            "status": "success",
            "scroll_to_contact": True,
            "posts": posts
        }
        return render(request, self.template_name, context)

