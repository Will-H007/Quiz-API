
from django.db import models
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles
from django.contrib.postgres.fields import JSONField

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Quiz_API(models.Model):
    question = models.CharField(max_length=100, default='')
    q_type = models.IntegerField(default=1)
    answers = models.JSONField(default=dict)
    validation = models.BooleanField(default=False)
