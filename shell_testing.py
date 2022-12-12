

# python manage.py shell


from API.models import Quiz_API
from API.serializers import Quiz_APISerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
  
# Opening JSON file
f = open('data.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
data = data[0]
quiz = Quiz_API(data=data)

quiz.save()


serializer = Quiz_APISerializer(quiz)
serializer.data

python manage.py makemigrations API
python manage.py migrate API

content = JSONRenderer().render(serializer.data)
content

import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)
serializer = Quiz_APISerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()