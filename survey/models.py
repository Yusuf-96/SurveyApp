from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.

class Choice(models.Model):
    choice = models.CharField(max_length=200)
    is_answered = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.choice}'

class Question(models.Model):
    question = models.CharField(max_length= 200)
    choices = models.ManyToManyField(Choice, related_name="choices")

    def addquestion(self):
        return reverse('survey:add_question', kwargs={'code':self.code})
    

    def __str__(self):
        return f'{self.question}'

class Answer(models.Model):
    answer = models.CharField(max_length= 500)
    answer_to = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.answer}'

class Survey(models.Model):
    code = models.CharField(max_length=30, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300, null=True, blank=True)
    questions = models.ManyToManyField(Question)
    created_at = models.DateTimeField(auto_now_add=True)
    is_submited = models.BooleanField(default = False)


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
         return f'{self.title}'

    def addtoquestion(self):
        return reverse('survey:Createsurvey', kwargs={'pk':self.pk})

class Response(models.Model):
    code = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    response = models.CharField(max_length=100)
    response_to = models.ForeignKey(Survey, on_delete = models.CASCADE)
    responses = models.ManyToManyField(Answer)

    def __str__(self):
        return f'{self.response}'



