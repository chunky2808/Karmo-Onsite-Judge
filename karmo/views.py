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
			
			if code.language=='c++' or code.language=='C++':
				cmd = 'g++ code.code'
				subprocess.call(cmd, shell=True)

			return HttpResponse("ok")
	else:
		form = NewTopicForm3()
	return render(request, 'code_snippet.html', {'form' : form})



