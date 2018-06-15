from django.shortcuts import render
import subprocess
from .models import Contest,Question,Testcase
from datetime import datetime
from .forms import NewTopicForm,NewTopicForm2,NewTopicForm3
from django.http import HttpResponse, HttpResponseNotFound
import os
from django.views.decorators.csrf import csrf_exempt
from .models import Code_Snippet
from src.settings import *

from django.core.files.base import ContentFile


from django.core.files.storage import default_storage

import random, string

from django.contrib.auth.decorators import login_required


#g++ -o output_file input_file

import os 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)


@login_required(login_url='/users/login/')
#Compiling,Running file and taking input as a file and generating output in file result.txt
#C++
def hii(request):
	
	#compilation
	cmd = 'g++ working_input.cpp -o a.out' #compiling c++ program
	p = subprocess.call(cmd, shell=True)
	#print(subprocess.check_output(cmd, shell=True))
	if p==0:
		print("Successfully running")
	else:
		print(subprocess.check_output(cmd, shell=True))
		print("Error")
	generate_input()
	return HttpResponse("ok")
	


#C++
#Compiling,Running file and taking input as a file and generating output in file result.txt



@login_required(login_url='/users/login/')
#checking difference of ouptput file of two files
def match_testcase(request):
	cmd = "diff result.txt true_result.txt"
	p = subprocess.call(cmd,shell=True)
	if p==0:
		return HttpResponse("Successfully running")
	else:
		print("Error")
		return HttpResponse("WA")
	
#checking difference of ouptput file of two files



#Python

@login_required(login_url='/users/login/')
def hi(request):
	
	#compilation
	cmd = 'python Compile_error.py' 
	p = subprocess.call(cmd, shell=True)
	prin
	#print(subprocess.check_output(cmd, shell=True))
	if p==0:
		print("Successfully running")
	else:
		print(subprocess.check_output(cmd, shell=True))
		print("Error")


#Python


@login_required(login_url='/users/login/')
#GIves compilation result for a code
@csrf_exempt
def take_input(request):
	if request.method == 'POST':
		form = NewTopicForm3(request.POST)
		if form.is_valid():
			new = form.save(commit=False)
			new.save()
			p = new.id
			code = Code_Snippet.objects.get(id = p)
			print(code.code)
			dir_path = BASE_DIR + '/code_compile'
			if not os.path.exists(dir_path):
				os.makedirs(dir_path, 0o777)
			file2write=open(BASE_DIR + '/code_compile/%s.cpp'%p,'w')
			file2write.write(code.code)
			file2write.close()
			file_path = BASE_DIR + '/code_compile/%s.cpp'%p
			if code.language=='c++' or code.language=='C++':
				cmd = 'g++ %s'%file_path
				status = subprocess.call(cmd, shell=True)
				if(status==1):
					print("Compilation Error")
					return HttpResponse("Compilation Error")
				else:
					print("Running Successfully")	
					return HttpResponse("Running Successfully")
	else:
		form = NewTopicForm3()
	return render(request, 'code_snippet.html', {'form' : form})
#GIves compilation result for a code


@login_required(login_url='/users/login/')
@csrf_exempt
def create_contest(request):
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			new = form.save(commit=False)
			print(request.user)
			new.created_by = request.user
			cmd = 'mkdir %s'%BASE_DIR + '/Contest'+ '/%s'%new.Name#create folder for contest Name
			print(cmd)
			subprocess.call(cmd, shell=True)

			new.save()
			return HttpResponse("Contest created Successfully")
	else:
		form = NewTopicForm()
	return render(request, 'create_contest.html', {'form' : form})


@login_required(login_url='/users/login/')
@csrf_exempt
def create_question(request):
	if request.method == 'POST':
		form = NewTopicForm2(request.POST)
		if form.is_valid():
			new = form.save(commit=False)
			print(request.user)
			
			cmd = 'mkdir %s/'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name #create folder for question name in contest
			subprocess.call(cmd, shell=True)
			

			cmd = 'mkdir %s/'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name + '/code_compile' #create folder code_compile for question in a contest
			subprocess.call(cmd, shell=True)


			cmd = 'mkdir %s/'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name + '/testcases' #create folder testcases for question in a contest
			subprocess.call(cmd, shell=True)

			cmd = 'mkdir %s/'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name + '/testcases/Input' #create folder testcases for question in a contest
			subprocess.call(cmd, shell=True)

			cmd = 'mkdir %s/'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name + '/testcases/Output' #create folder testcases for question in a contest
			subprocess.call(cmd, shell=True)			


			cmd = 'mkdir %s/'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name + '/question' #create folder question for question in a contest
			subprocess.call(cmd, shell=True)


			cmd = 'mkdir %s/'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name + '/solution' #create folder solution for question in a contest 
			subprocess.call(cmd, shell=True)

			cmd = 'mkdir %s/'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name + '/coreoperations' #create folder coreoperations for operations 
			subprocess.call(cmd, shell=True)


			#write question to a file in local
			file2write=open('%s'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name + '/question' + '/Question.txt','w')
			file2write.write(new.Prob_statement)
			file2write.close()
			#write question to a file in local

			#write question to a file in local
			file2write=open('%s'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name + '/solution' + '/Solution.cpp','w')
			file2write.write(new.solution)
			file2write.close()
			#write question to a file in local

			new.created_by = request.user

			new.save()
			return HttpResponse("Question Created")
	else:
		form = NewTopicForm2()
	return render(request, 'create_question.html', {'form' : form})


@login_required(login_url='/users/login/')
#Upload Input,Output Testcase for a question in a particular contest
def testcase(request,pk,pkk):
	question = Question.objects.get(pk=pkk)
	contest = Contest.objects.get(pk =pk)
	return render(request, 'upload_testcase.html',{'question':question,'contest':contest})

def testcase_main(request,pk,pkk):
	question = Question.objects.get(pk=pkk)
	contest = Contest.objects.get(pk =pk)	
	print(question)
	print(contest)
	if request.method == 'POST':
		files = request.FILES.getlist("file")
		folder = BASE_DIR + '/Contest/' + '%s/'%contest + '%s'%question +'/testcases'
		folder2 = '/Contest/' + '%s/'%contest + '%s'%question +'/testcases'
		print(folder)
		f=0
		test = Testcase.objects.create(contest=contest,question=question)
		#Added x for randomness in input output file name
		x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(4))
		for files in files:
			ext = files.name.split('.')[-1]
			if ext=='txt' or ext=='Txt':
				if f==0:#input file
					default_storage.save(folder + '/Input' + '/i1' + '%s'%x  +".txt", ContentFile(files.read()))
					print(Testcase.objects.filter(id = test.id))
					Testcase.objects.filter(id = test.id).update(inpt =(folder2 + '/Input' + '/i1' + '%s'%x  +".txt") )
				else:
					default_storage.save(folder + '/Output'+'/o1' + '%s'%x + ".txt", ContentFile(files.read()))
					Testcase.objects.filter(id = test.id).update(outp =(folder2 + '/Input' + '/i1' + '%s'%x  +".txt") )
				f = f+1	
	return HttpResponse("Uploaded Successfully")	
#Upload Input,Output Testcase for a question in a particular contest


@login_required(login_url='/users/login/')
#For single question
def question(request,pk,cont):
	question = Question.objects.get(pk=pk)
	contest = Contest.objects.get(pk =cont)
	print(contest)
	print(question)
	return render(request,'single_question.html',{'question':question,'contest':contest})
#For single question


@login_required(login_url='/users/login/')
#See all exsisting contests
def exsisting_contest(request):
	print(request.META['HTTP_HOST'])
	contest = Contest.objects.all()
	print(contest)
	return render(request,'exsisting_contest.html',{'contest':contest})
#See all exsisting contests


@login_required(login_url='/users/login/')
#To display all questions
def problem(request,pk):
	print(pk)
	contest = Contest.objects.filter(pk=pk)
	question = Question.objects.filter(contest=pk)
	print(question)
	for contest in contest:
		contests = contest
	return render(request,'problem.html',{'problem':question,'contest':contests})
#To display all questions	


@login_required(login_url='/users/login/')
#submit solution in contest
#file saving in code_compile folder for contest with name of user +id
def submit_problem_contest(request,pk,pkk):
	print("hi")
	contest = Contest.objects.get(pk=pk)
	question = Question.objects.get(pk=pkk)
	if request.method == 'POST':
		form = NewTopicForm3(request.POST)
		if form.is_valid():
			new = form.save(commit=False)
			new.save()
			p = new.id
			code = Code_Snippet.objects.get(id = p)
			print(code.code)
			dir_path = BASE_DIR + '/Contest/%s'%contest.Name + '/%s'%question.Name +'/code_compile'
			if not os.path.exists(dir_path):
				os.makedirs(dir_path, 0o777)
			nam = request.user
			compile_folder_path = BASE_DIR + '/Contest/%s'%contest.Name + '/%s'%question.Name +'/code_compile/%s'%nam + '%s'%p
			if not os.path.exists(compile_folder_path):
				os.makedirs(compile_folder_path, 0o777)
			file2write=open(compile_folder_path + '/%s'%name + '%s'%p + '.cpp','w')
			file2write.write(code.code)
			file2write.close()
			file_path = compile_folder_path +'/%s'%nam + '%s'%p + '.cpp'
			if code.language=='c++' or code.language=='C++':
				cmd = 'g++ %s'%file_path +" -o "+ compile_folder_path +'/%s'%nam + '%s'%p + '.out'
				status = subprocess.call(cmd, shell=True)
				if(status==1):
					print("Compilation Error")
					return HttpResponse("Compilation Error")
				else:
					print("Running Successfully")	
					generate_input()
	else:
		form = NewTopicForm3()
	return render(request, 'code_snippet.html', {'form' : form})	

#submit solution in contest


def generate_input():
	startTime = datetime.now()
	cmd = './a.out < /home/paras/Desktop/coding/my-project/Judge/input.txt > result.txt' #running a c++ program(name of file)

	#command to run code with input file ./test.exe input.txt
	
	p = subprocess.call(cmd, shell=True)
	if p==0:
		print("Successfully running")
	else:
		print(subprocess.check_output(cmd, shell=True))
		print("Error")

	print("Time taken in Judging")
	print(datetime.now() - startTime)
	#running




@login_required(login_url='/users/login/')
#Function to run file
def run_file():
	#running	
	print("hi")
	startTime = datetime.now()
	cmd = './a.out' #running a c++ program(name of file)

	#command to run code with input file ./test.exe input.txt
	
	p = subprocess.call(cmd, shell=True)
	if p==0:
		print("Successfully running")
	else:
		print(subprocess.check_output(cmd, shell=True))
		print("Error")

	print("Time taken in Judging")
	print(datetime.now() - startTime)
	#running

#Function to run file





