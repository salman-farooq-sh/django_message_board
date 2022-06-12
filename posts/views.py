from django.views.generic import ListView

from .models import Post


class HomePageView(ListView):
    def get_queryset(self):
        return Post.objects.order_by('-publication_date')
