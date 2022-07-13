from django.shortcuts import render
from django.views.generic import ListView
from mainapp.models import Durations
from .filters import DurationsFilter


class Index(ListView):
    model = Durations
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = DurationsFilter(self.request.GET, queryset=self.get_queryset())
    #     durations = Durations.objects.all
    #     context['durations'] = durations
    #     context['title'] = 'Главная'
    #     return context

    def get(self, request, *args, **kwargs):
        context = {
            'filter': DurationsFilter(self.request.GET, queryset=self.get_queryset()),
            'title': 'Главная',
        }
        if request.GET.get('client_id'):
            print(request.GET['client_id'])
        return render(request, self.template_name, context=context)



