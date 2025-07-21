from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Users
# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context["title"] = 'Home'
        context["user"] = {
            "name": "Mahesh Kumar",
            "city": "Dehradun",
            "country": "India",
        }
        return context


class UserDetail(DetailView):
    model = Users
    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context["template"] = self.get_template_names()
        return context