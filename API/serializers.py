from rest_framework import serializers
from API.models import Quiz_API



 
# create a serializer
class Quiz_APISerializer(serializers.ModelSerializer):
    # initialize fields
    class Meta:
        model = Quiz_API
        fields = ['id','question', 'answers','validation']