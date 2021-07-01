from django.db import models


class List(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)


class ListItem(models.Model):
    text = models.CharField(max_length=200, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    list = models.ForeignKey(List, verbose_name="List", on_delete=models.CASCADE, related_name='items')
    is_done = models.BooleanField(default=False)

