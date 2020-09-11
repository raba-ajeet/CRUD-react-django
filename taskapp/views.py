from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import task
from .serializers import taskSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.parsers import JSONParser 
# Create your views here.

@api_view(['GET'])
def task_list(request):
    tasks=task.objects.all().order_by('-id')
    serializer=taskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def task_detail(request,task_pk):
    task_obj=task.objects.get(pk=task_pk)
    serializer=taskSerializer(task_obj,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def task_create(request):
    serializer=taskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def task_update(request,task_pk):
    task_obj=task.objects.get(pk=task_pk)
    serializer=taskSerializer(instance=task_obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def task_delete(request,task_pk):
    task_obj=task.objects.get(pk=task_pk)
    task_obj.delete()
    return Response("It is deleted sucessfully")
    
