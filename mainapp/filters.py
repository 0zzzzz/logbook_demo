import django_filters
from mainapp.models import Durations, Clients, Equipment, Modes


class DurationsFilter(django_filters.FilterSet):
    client_id = django_filters.ChoiceFilter(choices=[], label='Клиент')
    equipment_id = django_filters.ChoiceFilter(choices=[], label='Оборудование')
    mode_id = django_filters.ChoiceFilter(choices=[], label='Состояние')
    minutes = django_filters.CharFilter(label='Длительность состояния')
    start = django_filters.DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y'],
                                      lookup_expr='contains', label='Дата начала')
    stop = django_filters.DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y'],
                                     lookup_expr='contains', label='Дата окончания')
    start_time = django_filters.NumberFilter(lookup_expr='gte', field_name='start__hour',
                                             label='Время начала, номер часа')
    end_time = django_filters.NumberFilter(lookup_expr='lte', field_name='stop__hour',
                                           label='Время окончания, номер часа')

    class Meta:
        model = Durations
        fields = ['client_id', 'equipment_id', 'mode_id', 'minutes', 'start', 'stop',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['client_id'].extra['choices'] = [
            (client.id, client.name)
            for client in Clients.objects.all()
        ]
        self.filters['equipment_id'].extra['choices'] = [
            (equipment.id, equipment.name)
            for equipment in Equipment.objects.all()
        ]
        self.filters['mode_id'].extra['choices'] = [
            (mods.id, mods.name)
            for mods in Modes.objects.all()
        ]


