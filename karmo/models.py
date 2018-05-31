from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from src import settings



class Contest(models.Model):
	Name = models.TextField(max_length=4000)
	Desc = models.TextField(max_length = 4000)
	Timings = models.DateTimeField()
	created_by = models.ForeignKey(User,related_name = 'cont_created_by')
	language_accepted = models.TextField(max_length = 4000)
	url_code  = models.TextField(null=True)

	def __str__(self):
		return self.Name



class Question(models.Model):
	contest = models.ForeignKey(Contest,related_name='contest')
	Name = models.TextField(max_length=4000)
	Prob_statement = models.TextField(max_length = 8000)
	sample_input = models.TextField(max_length = 8000)
	explanation = models.TextField(max_length=8000,null=True)
	created_by = models.ForeignKey(User,related_name = 'ques_created_by')
	no_of_submission = models.IntegerField(default = 0)
	url_code  = models.TextField(null=True)

	def __str__(self):
		return self.Name

class Code_Snippet(models.Model):
	code = models.TextField()
	language = models.CharField(default = '',max_length=224)
	
	def __str__(self):
		return self.code