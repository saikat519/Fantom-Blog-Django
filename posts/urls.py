from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexView.as_view(),name="index"),
    path('detail/<int:pk>/<slug:slug>',PostDetail.as_view(),name="detail"),
    path('category/<int:pk>/<slug:slug>',CategoryView.as_view(),name="category_detail"),
    path('tags/<slug:slug>',TagDetail.as_view(),name="tag_detail"),
    path('create-post/',CreatePostView.as_view(),name="create_post"),
    path('update-post/<int:pk>/<slug:slug>',UpdatePostView.as_view(),name="update_post"),
    path('delete-post/<int:pk>/<slug:slug>',DeletePostView.as_view(),name="delete_post"),
    path('search/',SearchView.as_view(),name='search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)