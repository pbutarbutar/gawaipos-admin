from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]


class State(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(
        'Country', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]


class City(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    state = models.ForeignKey(
        'State', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]


class Street(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    city = models.ForeignKey(
        'City', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]
