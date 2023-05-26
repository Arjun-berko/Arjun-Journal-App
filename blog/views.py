from django.shortcuts import render, get_object_or_404,get_list_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User




class PostListView(ListView):
    model=Post
    template_name="blog/home.html"
    context_object_name = "posts"
    ordering=['-title']
    paginate_by = 5


class UserPostListView(ListView):
    template_name="blog/userpostlist.html"
    context_object_name = "posts"
    paginate_by = 4

    def get_queryset(self):
        current_user_instance=get_object_or_404(User,username=self.kwargs.get("username"))
        return Post.objects.filter(author=current_user_instance).order_by('date_posted')

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context["username"]=get_object_or_404(User,username=self.kwargs.get("username"))
        return context



class PostDetailView(DetailView):
    model=Post
    template_name="blog/postdetail.html"






class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    fields=["title","content"]
    template_name = "blog/postcreate.html"

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=["title","content","date_posted"]
    template_name = "blog/postupdate.html"

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template_name = "blog/postdelete.html"
    success_url = reverse_lazy("home page")

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False




def about(request):
    return render(request,"blog/about.html",{"title":"About"})





