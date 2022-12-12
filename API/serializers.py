from rest_framework import serializers
from API.models import Quiz_API
from django.contrib.auth.models import User


 
# create a serializer
class Quiz_APISerializer(serializers.ModelSerializer):
    # initialize fields
    class Meta:
        model = Quiz_API
        fields = ['id',"q_type",'question', 'answers','validation']