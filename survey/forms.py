from django import forms
from django.forms import formset_factory 
from .models import Survey, Question, Choice


class SurveyForm(forms.ModelForm):
    
    class Meta:
        model = Survey

        exclude = ['user','is_submited']

        widgets = {
                    'title': forms.TextInput(
                        attrs={'class': 'form-input border-b-2 border-red-200 focus:outline-none block w-full focus:border-red-600 transition duration-700 py-2 ease-out',
                            'placeholder': 'Untitled Form'}
                        ),
                    'description': forms.TextInput(
                        attrs={
                            'class': 'form-input border-b-2 border-red-200 focus:outline-none block w-full focus:border-red-600 transition duration-700 py-2 ease-out',
                            'placeholder': 'From description'
                            }
                        ),
                }

        
    
class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question

        fields = ('question',)
        
        widgets = {
            'question': forms.TextInput(
                attrs = {
                    'class': 'form-input border-b-2 border-red-200 focus:outline-none block focus:border-red-600 w-full transition duration-700 py-2 ease-out ',
                    'placeholder':'Add your question'
                }
            )
           
        }

# class ChoiceForm(forms.ModelForm):
#     class Meta:
#         model = Choice
#         exclude =['user', 'is_answered']

#         fields = ('choice',)

        # widgets = {
        #     'choice': forms.TextInput(
        #         attrs = {
        #             'class': 'form-input border-b-2 border-red-200 focus:outline-none block focus:border-red-600 w-full transition duration-700 py-2 ease-out'
        #         }
        #     )
        # }






            