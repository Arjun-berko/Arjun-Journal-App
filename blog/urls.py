from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView, PostDeleteView, PostUpdateView, UserPostListView

urlpatterns=[path('about',views.about,name='about page'),
             path('postlist',PostListView.as_view(),name="home page"),
             path('postlist/<str:username>/',UserPostListView.as_view(),name="user posts"),
             path('postdetail/<int:pk>/',PostDetailView.as_view(),name="post detail"),
             path('postupdate/<int:pk>/',PostUpdateView.as_view(),name="post update"),
             path('post/new/',PostCreateView.as_view(),name="post create"),
             path('post/delete/<int:pk>/',PostDeleteView.as_view(),name="post delete")]

# path('postlist',PostListView.as_view(),name="home page"),