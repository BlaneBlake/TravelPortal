"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import (
    Test,
    HomePageView,
    PostCreateView,
    PostEditView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    UserPostListView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/all-posts', PostListView.as_view(), name='post_list'),
    path('post/your-posts', UserPostListView.as_view(), name='user_post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('blog_test/', Test.as_view(), name='test'),
    ]