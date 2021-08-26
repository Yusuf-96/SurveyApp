from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from .models import Survey, Question, Choice, Response, Answer
from .forms import SurveyForm, QuestionForm
from django.forms import formset_factory
from django.contrib.auth.models import User
import random
import string
import json
# Create your views here.

class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        template_name = 'surveys/index.html',
        survey=Survey.objects.all().count()
        context = {
            'total_survey': survey
        }
        return render (request, template_name, context)


class CreateSurvey(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        template_name = 'surveys/surveypage.html'
        return render(request, template_name)


        
        

    def post(self, request, *args, **kwargs):
        if request.method =="POST":
            code = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(30))
            title = request.POST['title']
            description = request.POST['description']
            form = Survey(code=code, title=title, description=description, user=request.user)
            form.save()
            for qname in request.POST.getlist('question'): 
                question = Question.objects.create(question=qname)
                question.save()
                form.questions.add(question)
                form.save()
            # qs = Question.objects.filter(question=question)
            # if qs.exists():
                for name in request.POST.getlist('choice'):
                    options = Choice.objects.create(choice=name)
                    options.save()
                    question.choices.add(options)
                    question.save()
            print('form save successuful')
            print(request.POST)
            return redirect('survey:survey-view')
        return redirect('survey:survey-page')


class UpdateSurvey(LoginRequiredMixin, View):
    def get(self, request, *args,code, **kwargs):
        survey = Survey.objects.get(code=code)
        question = Question.objects.filter(survey=survey).first()
        template_name = 'surveys/surveyupdate.html'
        form = SurveyForm(instance=survey)
        qform = QuestionForm(instance=question)
        context = {
            'form':form,
            'qform':qform,
            'survey':survey
        }
        return render(request, template_name, context)
    def post(self, request, *args, code, **kwargs):
        survey = Survey.objects.get(code=code)
        question = question.objects.get(pk=survey)
        form = SurveyForm(request.POST, instance=survey)
        qfrom = QuestionForm(request.POST, instance = question)
        if request.method == 'POST':
            form = SurveyForm(request.POST, instance=survey)
            qform = QuestionForm(request.POST, instance = question)
            if form.is_valid() and qform.is_valid():
                form.save()
                qform.save()
                print('Your survey has been updated')
                return redirect('survey:survey-view')
        else:
            print("something is wrong with your form")
            return redirect('survey:survey-update')
        
        
        
class SurveyDetails(View):
    def get(self, request, code, *args,**kwargs):
        try:
            surveys = Survey.objects.get(code=code)
            questions = Question.objects.all().filter(survey=surveys)
            template_name = 'surveys/surveydetails.html'
            context = {
                'surveylist':surveys,
                'questions':questions,
            }

            return render(request, template_name, context)

        except ObjectDoesNotExist:
            return redirect('/')

    def post(self, request, *args,code, **kwargs):
        survey = Survey.objects.filter(code=code, user=request.user, is_submited = False)   
        if request.method == 'POST':
            code = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(20))
            response = Response.objects.create(code=code, response_to=survey, user=request.user)
            response.save()
            for i in request.POST:
                question = survey.Question.get(id=i)
                for choice in request.POST.getlist(i):
                    answer = Answer.objects.create(answer= choice, answer_to= question)
                    answer.save()
                    response.responses.add(answer)
                    response.save()
            print('Your form submited')
            return redirect('survey:survey-view')
        return redirect('survey:survey-detail')


class SurveyView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        template_name = 'surveys/viewsurveypage.html'
        surveys = Survey.objects.filter(user=request.user)
        context = {
            'surveylist': surveys
        }
        return render(request, template_name, context)


        
            




    




