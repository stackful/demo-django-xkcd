from __future__ import absolute_import, division, print_function, unicode_literals
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "main/home.html"
