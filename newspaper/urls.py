from django.urls import path
from newspaper import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("post-detail/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
]
