from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import TipoCambio,Producto# Import the task function from tasks.py
# from .forms import TareaForm
# import requests
# import json
from django.http import JsonResponse
# from user.models import User
import os

from .models import Task, Link
from .serializers import TaskSerializer, LinkSerializer

from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.parsers import JSONParser
from django.core.mail import send_mail


@api_view(['GET'])
@csrf_exempt
def data_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        links = Link.objects.all()
        task_data = TaskSerializer(tasks, many=True).data
        link_data = LinkSerializer(links, many=True).data
        return Response({
            "tasks": task_data,
            "links": link_data
        })


@api_view(['POST'])
@csrf_exempt
def task_add(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            return JsonResponse({'action': 'inserted', 'tid': task.id})
        return JsonResponse({'action': 'error'})


@api_view(['PUT', 'DELETE'])
@csrf_exempt
def task_update(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return JsonResponse({'action': 'tarea no existe'})

    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'action': 'updated'})
        else:
            errors = serializer.errors
            return JsonResponse({'action': 'error en la edicion', 'errors': errors}, status=400)

    if request.method == 'DELETE':
        task.delete()
        return JsonResponse({'action': 'deleted'})


@api_view(['POST'])
@csrf_exempt
def link_add(request):
    if request.method == 'POST':
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            link = serializer.save()
            return JsonResponse({'action': 'inserted', 'tid': link.id})
        return JsonResponse({'action': 'error'})


@api_view(['PUT', 'DELETE'])
@csrf_exempt
def link_update(request, pk):
    try:
        link = Link.objects.get(pk=pk)
    except Link.DoesNotExist:
        return JsonResponse({'action': 'error'})

    if request.method == 'PUT':
        serializer = LinkSerializer(link, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'action': 'updated'})
        return JsonResponse({'action': 'error'})

    if request.method == 'DELETE':
        link.delete()
        return JsonResponse({'action': 'deleted'})


# Funcion INDEX
def index(request):
    title = 'HOME'
    return render(request, 'gantt/index.html', {
        'title': title
    })

