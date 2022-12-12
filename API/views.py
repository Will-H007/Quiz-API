from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from API.models import Quiz_API
from API.serializers import Quiz_APISerializer
from random import choice


@csrf_exempt
def Quiz_API_list(request, answer = None):
    """
    List all code quiz, or create a new quiz.
    """
    # User requesting quiz
    if request.method == 'GET':
        quiz = Quiz_API.objects.filter(validation=False)  
        serializer = Quiz_APISerializer(quiz, many=True)
        return JsonResponse(choice(serializer.data), safe=False)

        
    # Uploading data to the database
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Quiz_APISerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



    # Modifying the validation of the quiz if the user gets the answer correctly so that the user won't get the same question again
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Quiz_APISerializer(data=data) 
        instances = Quiz_API.objects.filter(id = data['id']).first()
        if serializer.is_valid():
            if instances.answers == serializer.data['answers']:
                serializer.data['validation'] = True
                serializer.update(instance = instances, validated_data=serializer.data)
                return HttpResponse("Congrates! You got it right!")
            else:
                return HttpResponse("Sorry you got it wrong.")
        return JsonResponse(serializer.errors, status=400)


