from django.urls import path
from .views import *
from django.contrib.auth import views as authViews
app_name = "users"
urlpatterns = [
    path('',UserListView.as_view(),name="user_list"),
    path('register/',RegisterView.as_view(),name="register"),
    path('login/',UserLoginView.as_view(),name="login"),
    path('logout/',UserLogoutView.as_view(),name="logout"),
    path('change-password/',authViews.PasswordChangeView.as_view(),name="password_change"),
    path('change-password-done/',authViews.PasswordChangeDoneView.as_view(),name="change_password_done"),
    path('update-profile/<slug:slug>/',UserProfileUpdateView.as_view(),name="update_profile"),
    path('my-profile/',UserProfileView.as_view(),name="my-profile"),
    path('<int:pk>/',UserPostView.as_view(),name="user_posts"),

]