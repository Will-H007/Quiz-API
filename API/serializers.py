from rest_framework import serializers
from API.models import Quiz_API



 
# create a serializer
class Quiz_APISerializer(serializers.ModelSerializer):
    # initialize fields
    class Meta:
        model = Quiz_API
        fields = ['question', 'answers','validation']
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Quiz_API` instance, given the validated data.
    #     """
    #     return Quiz_API.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Quiz_API` instance, given the validated data.
    #     """
    #     instance.question = validated_data.get('question', instance.question)
    #     instance.answers = validated_data.get('answers', instance.answers)
    #     instance.validation = validated_data.get('validation', instance.validation)
   
    #     instance.save()
    #     return instance