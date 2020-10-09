from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from src import settings
import datetime


class Contest(models.Model):
	Name = models.TextField(max_length=4000,unique=True)
	Desc = models.TextField(max_length = 4000)
	Timings = models.CharField(max_length=244)
	created_by = models.ForeignKey(User,related_name = 'cont_created_by')
	language_accepted = models.TextField(max_length = 4000)
	url_code  = models.TextField(null=True)
	date = models.CharField(max_length=244)
	score = models.IntegerField(default = 0)

	def __str__(self):
		return self.Name

	def __unicode__(self):
		return self.Name.replace('_', ' ')	



class Question(models.Model):
	contest = models.ForeignKey(Contest,related_name='contest')
	Name = models.TextField(max_length=4000)
	Prob_statement = models.TextField(max_length = 8000)
	sample_input = models.TextField(max_length = 8000)
	explanation = models.TextField(max_length=8000,null=True)
	created_by = models.ForeignKey(User,related_name = 'ques_created_by')
	no_of_submission = models.IntegerField(default = 0)
	solution = models.TextField(default ='')
	url_code  = models.TextField(null=True)

	def __str__(self):
		return self.Name

class Code_Snippet(models.Model):
	code = models.TextField()
	language = models.CharField(default = '',max_length=224)
	
	def __str__(self):
		return self.code

class Testcase(models.Model):
	contest = models.ForeignKey(Contest,related_name='testcase_contest')
	question = models.ForeignKey(Question,related_name = 'testcase_ques')
	inpt = models.TextField()#path	
	outp = models.TextField()#path
	
	def __unicode__(self):
		return self.id



class Submit_Question(models.Model):#user model for submission of question
	user = models.ForeignKey(User,related_name='submitted_by')
	contest = models.ForeignKey(Contest,related_name='submit_contest')
	question = models.ForeignKey(Question,related_name = 'submit_ques')
	verdict = models.IntegerField(default = 0)#2 for TLE
	start_time = models.TimeField(default=datetime.datetime.now().time())
	end_time = models.TimeField(default=datetime.datetime.now().time())

	def __unicode__(self):
		return self.id

	class Contest2(models.Model):
	Name = models.TextField(max_length=4000,unique=True)
	Desc = models.TextField(max_length = 4000)
	Timings = models.CharField(max_length=244)
	created_by = models.ForeignKey(User,related_name = 'cont_created_by')
	language_accepted = models.TextField(max_length = 4000)
	url_code  = models.TextField(null=True)
	date = models.CharField(max_length=244)
	score = models.IntegerField(default = 0)

	def __str__(self):
		return self.Name

	def __unicode__(self):
		return self.Name.replace('_', ' ')	
class User_score(models.Model):
	user = models.ForeignKey(User,related_name='user_y')
	score = models.IntegerField(default=0)
	contest = models.ForeignKey(Contest,related_name='submit_contestt',default=1)
	time = models.TimeField(default=datetime.datetime.now().time())
	
	def __unicode__(self):
		return self.id

class Category(models.Model):
    name = models.CharField(max_length=100,default='Student')

    def __str__(self):
        return self.name


class Karmouser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.user.username


class Student(models.Model):
    name = models.CharField(max_length=100,default='Student')

    def __str__(self):
        return self.name
