from django import forms
from .models import Contest,Question,Code_Snippet

Languages= [
    ('c++','C++'),
    ('c++ 14','C++ 14'),
    ('c','C'),
    ('python2','Python2'), 
    ('python3','Python3'),
    ('java','Java'),
    ('java 8','Java 8')
    ]

class NewTopicForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ['Name','Desc','date','Timings','language_accepted','url_code']


class NewTopicForm2(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['contest','Name','Prob_statement','solution','sample_input','explanation','created_by','no_of_submission','url_code']


class NewTopicForm3(forms.ModelForm):
	code = forms.CharField(widget=forms.Textarea(attrs={'cols': 200, 'rows': 50}))
	language= forms.CharField(label='Language', widget=forms.Select(choices=Languages))
	Name_of_File = forms.CharField()
	class Meta:
		model = Code_Snippet
		fields = ['code','language','Name_of_File']

