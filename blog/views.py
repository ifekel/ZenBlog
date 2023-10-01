from django.shortcuts import render
from .models import Blog, Category
from django.views.generic import ListView, DetailView, TemplateView
import os
from dotenv import load_dotenv

load_dotenv()


# Home Page View
class HomePageView(ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.order_by('?')[:10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        APP_NAME = os.getenv('APP_NAME')

        context['APP_NAME'] = APP_NAME
        return context


class CategoryPageView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        APP_NAME = os.getenv('APP_NAME')

        context['APP_NAME'] = APP_NAME
        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        APP_NAME = os.getenv('APP_NAME')

        context['APP_NAME'] = APP_NAME
        return context


class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        APP_NAME = os.getenv('APP_NAME')

        context['APP_NAME'] = APP_NAME
        return context


class BlogDetailPageView(DetailView):
    model = Blog
    template_name = "single-post.html"
    context_object_name = 'blog'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        APP_NAME = os.getenv('APP_NAME')

        context['APP_NAME'] = APP_NAME
        return context