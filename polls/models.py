import datetime

from django.db import models
from django.utils import timezone

# Each model is represented by a class that subclasses django.db.models.Model.

class Question(models.Model):
    # Each field is represented by an instance of a Field class
    # CharField and DateTimeField tell Django what type of data each field holds.
    # question_text or pub_date are the field’s name.
    #  Use this value in Python code, and database will use it as the column name.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # 
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # A relationship is defined, using ForeignKey. That tells Django each Choice is related to a single Question. 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text