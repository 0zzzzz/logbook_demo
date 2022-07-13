from django.db import models


class Clients(models.Model):
    name = models.TextField(null=False)

    class Meta:
        db_table = 'clients'


class Equipment(models.Model):
    client_id = models.ForeignKey(Clients, null=False, default=1, on_delete=models.CASCADE)
    name = models.TextField(null=False)

    class Meta:
        db_table = 'equipment'


class Modes(models.Model):
    name = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        db_table = 'modes'


class Durations(models.Model):
    client_id = models.ForeignKey(Clients, null=False, on_delete=models.CASCADE)
    equipment_id = models.ForeignKey(Equipment, null=False, on_delete=models.CASCADE)
    mode_id = models.ForeignKey(Modes, null=False, on_delete=models.CASCADE)
    start = models.DateTimeField(null=False)
    stop = models.DateTimeField(null=False)
    minutes = models.IntegerField(null=False)

    class Meta:
        db_table = 'durations'


