from rest_framework import serializers
from list.models import List, ListItem


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'title', 'created', 'items']
        depth = 1


class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItem
        fields = ['id', 'text', 'created', 'list', 'is_done']
