from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home_page"),
    path('category/', views.CategoryPageView.as_view(), name="category_page"),
    path('about/', views.AboutPageView.as_view(), name="about_page"),
    path('contact/', views.ContactPageView.as_view(), name="contact_page"),
    path('blog/<uuid:blog_id>/', views.BlogDetailPageView.as_view(), name="blog_item"),
]
