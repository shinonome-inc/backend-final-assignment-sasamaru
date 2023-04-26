# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# from .models import Tweet


class HomeView(TemplateView):
    # model = Tweet
    template_name = "tweets/home.html"
