from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from API.models import Quiz_API
from API.serializers import Quiz_APISerializer
from random import choice
# Create your views here.

@csrf_exempt
def Quiz_API_list(request):
    """
    List all code quiz, or create a new quiz.
    """
    if request.method == 'GET':
        quiz = Quiz_API.objects.all()
        serializer = Quiz_APISerializer(quiz, many=True)
        print(serializer.data)
        quiz = Quiz_API.objects.filter(validation=False)  
        serializer = Quiz_APISerializer(quiz, many=True)
        return JsonResponse(choice(serializer.data), safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Quiz_APISerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Quiz_APISerializer(data=data) 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def Quiz_API_detail(request, pk):
#     """
#     Retrieve, update or delete a code Quiz_API.
#     """
#     try:
#         Quiz_API = Quiz_API.objects.get(pk=pk)
#     except Quiz_API.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = Quiz_APISerializer(Quiz_API)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = Quiz_APISerializer(Quiz_API, data=data)
#         # print(serializer.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         Quiz_API.delete()
#         return HttpResponse(status=204)