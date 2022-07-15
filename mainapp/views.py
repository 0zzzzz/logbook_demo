from django.shortcuts import render
from django.views.generic import ListView
from mainapp.models import Durations
from .filters import DurationsFilter


class Index(ListView):
    model = Durations
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'filter': DurationsFilter(self.request.GET, queryset=self.get_queryset()),
            'title': 'Главная',
        }
        return render(request, self.template_name, context=context)
