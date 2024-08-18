from newspaper.models import Post

from django.views.generic import ListView


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

        return context
