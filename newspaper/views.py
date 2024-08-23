from newspaper.models import Category, Post, Tag

from django.views.generic import ListView, DetailView
from datetime import timedelta

from django.utils import timezone


class HomeView(ListView):
    model = Post
    template_name = "aznews/home.html"
    context_object_name = "posts"
    queryset = Post.objects.filter(published_at__isnull=False, status="active")[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["featured_post"] = (
            Post.objects.filter(published_at__isnull=False, status="active")
            .order_by("-published_at", "-views_count")
            .first()
        )
        context["featured_posts"] = Post.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-published_at", "-views_count")[1:4]

        one_week_ago = timezone.now() - timedelta(days=7)
        context["weekly_top_posts"] = Post.objects.filter(
            published_at__isnull=False, status="active", published_at__gte=one_week_ago
        ).order_by("-published_at", "-views_count")[:7]

        context["recent_posts"] = Post.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-published_at")[:7]

    
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "aznews/detail/detail.html"
    context_object_name = "post"

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(published_at__isnull=False, status="active")
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        obj.views_count += 1
        obj.save()

        # 7 => 1, 2, ,3 ,4 ,5, 6 => 6, 5, 4, 3, 2, 1
        context["previous_post"] = (
            Post.objects.filter(
                published_at__isnull=False, status="active", id__lt=obj.id
            )
            .order_by("-id")
            .first()
        )

        # 8, 9 , 10 ....
        context["next_post"] = (
            Post.objects.filter(
                published_at__isnull=False, status="active", id__gt=obj.id
            )
            .order_by("id")
            .first()
        )

        return context
