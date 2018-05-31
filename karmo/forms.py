from django import forms
from .models import Contest,Question,Code_Snippet

class NewTopicForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ['Name','Desc','Timings','language_accepted','url_code']


class NewTopicForm2(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['contest','Name','Prob_statement','sample_input','explanation','created_by','no_of_submission','url_code']


class NewTopicForm3(forms.ModelForm):
    class Meta:
        model = Code_Snippet
        fields = ['code','language']