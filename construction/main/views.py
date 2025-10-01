from django.shortcuts import render , HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):

        return render(request, self.template_name , {"status" : "success" , "scroll_to_contact": True})
