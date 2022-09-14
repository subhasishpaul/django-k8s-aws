from django.shortcuts import render
from .models import Blog
from django.views.generic import TemplateView # Import TemplateView

# Create your views here.
def blog(request):
	blogs = Blog.objects.all() #queryset containing all movies we just created
	return render(request=request, template_name="blog/blogs.html", context={'blogs':blogs})

# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "blog/index.html"


class AboutPageView(TemplateView):
    template_name = "blog/about.html"


class CloudView(TemplateView):
    template_name = "blog/cloud.html"