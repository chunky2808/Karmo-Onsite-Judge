from django.shortcuts import render
import subprocess
from .models import Contest,Question
from datetime import datetime
from .forms import NewTopicForm,NewTopicForm2,NewTopicForm3
from django.http import HttpResponse, HttpResponseNotFound
import os
from django.views.decorators.csrf import csrf_exempt
from .models import Code_Snippet
from src.settings import *

from django.core.files.base import ContentFile


from django.core.files.storage import default_storage


#g++ -o output_file input_file

import os 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

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

	#compilation
	run_file()
	

def run_file():
	#running	

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
	match_testcase()

def match_testcase():
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
#C++


#Python

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
			file2write=open('/home/paras/Desktop/coding/my-project/Judge/code_compile/%s.cpp'%p,'w')
			file2write.write(code.code)
			file2write.close()
			file_path = '/home/paras/Desktop/coding/my-project/Judge/code_compile/%s.cpp'%p
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


@csrf_exempt
def create_contest(request):
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			new = form.save(commit=False)
			print(request.user)
			new.created_by = request.user
			cmd = 'mkdir %s'%BASE_DIR + '/Contest'+ '/%s'%new.Name
			print(cmd)
			subprocess.call(cmd, shell=True)

			cmd = 'mkdir %s'%BASE_DIR + '/Contest'+ '/%s'%new.Name + '/code_compile'
			subprocess.call(cmd, shell=True)


			cmd = 'mkdir %s'%BASE_DIR + '/Contest'+ '/%s'%new.Name + '/testcases'
			subprocess.call(cmd, shell=True)

			new.save()
			return HttpResponse("Contest created Successfully")
	else:
		form = NewTopicForm()
	return render(request, 'create_contest.html', {'form' : form})


@csrf_exempt
def create_question(request):
	if request.method == 'POST':
		form = NewTopicForm2(request.POST)
		if form.is_valid():
			new = form.save(commit=False)
			print(request.user)
			cmd = 'mkdir %s/'%BASE_DIR + '/Contest'+ '/%s'%new.contest  + '/code_compile' +'/%s'%new.Name
			print(cmd)
			subprocess.call(cmd, shell=True)
			new.created_by = request.user

			new.save()
			return HttpResponse("Question Created")
	else:
		form = NewTopicForm2()
	return render(request, 'create_question.html', {'form' : form})


def testcase(request):
	return render(request, 'upload_testcase.html')

def testcase_main(request):
	if request.method == 'POST':
		files = request.FILES.getlist("file")
		folder = BASE_DIR + '/Contest/' + '/Enigma18.1/output'
		f=0
		for files in files:
			if f==0:#input file
				default_storage.save(folder + '/' + files.name +".txt", ContentFile(files.read()))
			else:
				default_storage.save(folder + '/' + files.name +".txt", ContentFile(files.read()))	
			print(files)
	return HttpResponse("hi")	
