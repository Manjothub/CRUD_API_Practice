from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status


@api_view(['GET','POST'])
def books_collection(request):
    if request.method == 'GET':
        queryset = Bookslibrarry.objects.all()
        if queryset:
            data = Bookserializer(queryset,many=True)
            return JsonResponse({"Status":True, "data":data.data}, status=status.HTTP_200_OK)
    return JsonResponse({"Status": False, "Message":"Data Not Found"},status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def add_books_collection(request):
    if request.method == 'POST':
        queryset = Bookserializer(data=request.data)
        if queryset.is_valid():
            queryset.save()
            return JsonResponse({"Status":True, "data":queryset.data}, status=status.HTTP_200_OK)
        return JsonResponse({"Status": False, "Message":"Data Not Found"},status=status.HTTP_204_NO_CONTENT)