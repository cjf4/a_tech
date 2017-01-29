from django.contrib import admin

from .models import Survey, Question, QuestionOrder

survey_models = [Survey, Question, QuestionOrder]

admin.site.register(survey_models)
