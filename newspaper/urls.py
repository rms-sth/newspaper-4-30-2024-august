from django.urls import path
from newspaper import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("post-detail/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post-comment/", views.CommentView.as_view(), name="post-comment"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("post-list/", views.PostListView.as_view(), name="post-list"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]
