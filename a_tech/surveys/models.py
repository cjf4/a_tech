from django.db import models
from django.utils import timezone

class Survey(models.Model):
    survey_name = models.CharField(max_length=50)
    survey_description = models.CharField(max_length=1000)
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated', null = True)
    def __str__(self):
        return self.survey_name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    date_created = models.DateTimeField('date created', default = timezone.now)
    def __str__(self):
        return self.question_text

class QuestionOrder(models.Model):
    question_id = models.ForeignKey(Question, on_delete = models.CASCADE)
    survey_id = models.ForeignKey(Survey, on_delete = models.CASCADE)
    order = models.IntegerField()
