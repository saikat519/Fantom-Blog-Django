from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator

from .forms import *
from django.views.generic import CreateView, UpdateView, ListView

from posts.models import Post


class RegisterView(CreateView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = '/'


class UserLoginView(LoginView):
    template_name = "login.html"


class UserLogoutView(LogoutView):
    template_name = "login.html"


@method_decorator(login_required(login_url='/users/login'), name="dispatch")
class UserProfileUpdateView(UpdateView):
    model = UserProfile
    template_name = 'profile-update.html'
    form_class = UserProfileForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(UserProfileUpdateView, self).form_valid(form)

    def get(self,request,*args,**kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return HttpResponseRedirect('/')
        return super(UserProfileUpdateView, self).get(request,*args,**kwargs)


@method_decorator(login_required(login_url='/users/login'), name="dispatch")
class UserProfileView(ListView):
    template_name = 'my-profile.html'
    model = Post
    context_object_name = 'userposts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(UserProfileView,self).get_context_data(**kwargs)
        context['userprofile']=UserProfile.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user).order_by('-id')


class UserPostView(ListView):
    template_name = 'user-post.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 5


    def get_queryset(self):
        return Post.objects.filter(user=self.kwargs['pk'])


class UserListView(ListView):
    template_name = 'user-list.html'
    model = UserProfile
    context_object_name = 'profiles'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context=super(UserListView, self).get_context_data(**kwargs)
        return context