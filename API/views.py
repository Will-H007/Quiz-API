from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from API.models import Quiz_API
from API.serializers import Quiz_APISerializer
import json
from random import choice

def confirmation(text):
    response = {"message": text}
    return response
    

@csrf_exempt
def Quiz_API_list(request, answer = None):
    """
    List all code quiz, or create a new quiz.
    """
    # User requesting quiz
    if request.method == 'GET':
        quizs = Quiz_API.objects.filter(validation=False)  
        serializer = Quiz_APISerializer(quizs, many=True)
        quiz = choice(serializer.data)
        quiz['answers'] = dict.fromkeys(quiz['answers'],False)
        return JsonResponse(quiz, safe=False)

        
    # Uploading data to the database
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Quiz_APISerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            text =  confirmation("Successfully uploaded")
            return JsonResponse(text, status=201)
        return JsonResponse(serializer.errors, status=400)



    # Replying to the user regarding whether they got the answer correct or not
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Quiz_APISerializer(data=data) 
        instances = Quiz_API.objects.filter(id = data['id']).first()
        if serializer.is_valid():
            if instances.answers == serializer.data['answers']:
                serializer.update(instance = instances, validated_data=serializer.data)
                if instances.q_type == 1:
                    text =  confirmation("Congrates! You got it right! You have earned 2 points")
                else:
                    text =  confirmation("Congrates! You got it right! You have earned 3 points")
                return JsonResponse(text, status=201)
            else:
                text =  confirmation("Sorry wrong answer!")
                return JsonResponse(text, status=201)
        return JsonResponse(serializer.errors, status=400)


