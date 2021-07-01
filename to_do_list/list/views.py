from list.models import List, ListItem
from list.serializers import ListSerializer, ListItemSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse


@api_view(['GET', 'POST'])
def lists(request, list_pk=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        if list_pk:
            resp = List.objects.get(id=list_pk)
            serializer = ListSerializer(resp, many=False)
            return Response(serializer.data)
        else:
            resp = List.objects.all()
            serializer = ListSerializer(resp, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def lists_items(request, list_pk, item_pk=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        if item_pk:
            resp = ListItem.objects.get(id=item_pk)
            serializer = ListItemSerializer(resp, many=False)
            return Response(serializer.data)
        else:
            resp = ListItem.objects.filter(list_id=list_pk)
            serializer = ListItemSerializer(resp, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ListItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        try:
            snippet = ListItem.objects.get(id=item_pk)
        except ListItem.DoesNotExist:
            return HttpResponse(status=404)
        data = JSONParser().parse(request)
        serializer = ListItemSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        resp = ListItem.objects.get(id=item_pk)
        resp.delete()
        return HttpResponse(status=204)
