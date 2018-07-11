from django.shortcuts import render
import subprocess
from subprocess import STDOUT, check_output
from .models import Contest,Question,Testcase,Submit_Question
from .forms import NewTopicForm,NewTopicForm2,NewTopicForm3
from django.http import HttpResponse, HttpResponseNotFound
import os
from django.views.decorators.csrf import csrf_exempt
from .models import Code_Snippet
from src.settings import *
from subprocess import STDOUT, check_output

from django.core.files.base import ContentFile

from django.core.files.storage import default_storage

import random, string

from django.contrib.auth.decorators import login_required

import os 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

from datetime import datetime


#g++ -o output_file input_file
#cmd = 'g++ working_input.cpp -o a.out' #compiling c++ program
#cmd = './a.out < /home/paras/Desktop/coding/my-project/Judge/input.txt > result.txt' #running a c++ program(name of file)



language = {'python' : '.py','Python' : '.py', 'C++' : '.cpp' ,'C' : '.c'}

@login_required(login_url='/users/login/')
#Compiling,Running file and taking input as a file and generating output in file result.txt
#C++
def hii(request):
	#compilation
	cmd = ['g++','/home/paras/Desktop/coding/my-project/Judge/working_input.cpp','-o','a.out']
	
	try:
		p = subprocess.run(cmd,timeout=1)
		print(p,"HI")
		if p.returncode==0:
			print("Successfully Compiled")
		else:
			print("Error")
		return generate_input()
	except subprocess.TimeoutExpired:
		print('Timeout')
		return HttpResponse("TLE Timeout",datetime.now() - startTime)


def generate_input():
	startTime = datetime.now()
	print("hi")
	cmd = './a.out'
	#command to run code with input file ./test.exe input.txt

	try:
		p = subprocess.run(cmd,timeout=1)
		print(p,"HI")	
		if p.returncode==0:
			print("Successfully Compiled")
		else:
			print("Error")
			return HttpResponse("Compilation Error")
		print("Time taken in Judging")
		print(datetime.now() - startTime)
		return HttpResponse("Code Running",datetime.now() - startTime)
	except subprocess.TimeoutExpired:
		print('Timeout')
		return HttpResponse("TLE Timeout",datetime.now() - startTime)

	#running
#C++
#Compiling,Running file and taking input as a file and generating output in file result.txt




@login_required(login_url='/users/login/')
#checking difference of ouptput file of two files
def match_testcase(request):
	cmd = "diff -w result.txt true_result.txt"
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
	#print(subprocess.check_output(cmd, shell=True))
	if p==0:
		print("Successfully running")
		return HttpResponse("ok")
	else:
		#print(subprocess.check_output(cmd, shell=True))
		print("Error")
		return HttpResponse("Compilation Error")


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
		#x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(4))
		for files in files:
			ext = files.name.split('.')[-1]
			if ext=='txt' or ext=='Txt':
				if f==0:#input file
					default_storage.save(folder + '/Input' + '/i' + '%s'%str(test.id)  +".txt", ContentFile(files.read()))
					print(test.id)
					print(Testcase.objects.filter(id = test.id))
					Testcase.objects.filter(id = test.id).update(inpt =(folder2 + '/Input' + '/i' + '%s'%str(test.id)  +".txt") )
				else:
					default_storage.save(folder + '/Output'+'/o' + '%s'%str(test.id) + ".txt", ContentFile(files.read()))
					Testcase.objects.filter(id = test.id).update(outp =(folder2 + '/Output' + '/o' + '%s'%str(test.id)  +".txt") )
				f = f+1	
	if f==0:
		return HttpResponse("Not uploaded test cases only .txt files allowed")
	else:			
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


#To display all questions
'''
logic to display solved question using flag of verdict =1 and for unsolved question taking all question in a set and removing solved question from set.
'''
@login_required(login_url='/users/login/')
def problem(request,pk):
	contest = Contest.objects.filter(pk=pk)
	question = Question.objects.filter(contest=pk)
	user = request.user
	
	solved_question = Submit_Question.objects.filter(user=user,contest=contest,question=question,verdict=1)
	
	my_set = set()
	for solved_question in solved_question:
		my_set.add(solved_question.question)
	
	print(my_set)

	for contest in contest:
		contests = contest
	return render(request,'problem.html',{'contest':contests,'question':question,'my_set':my_set})



@login_required(login_url='/users/login/')
#submit solution in contest
#file saving in code_compile folder for contest with name of user +id
def submit_problem_contest(request,pk,pkk):
	startTime = datetime.now()
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
			if is_safe(code.code,code.language)==False:
				return HttpResponse("We find something Malicious in your code .Please Contact Admin.")
			print(code.language)
			dir_path = BASE_DIR + '/Contest/%s'%contest.Name + '/%s'%question.Name +'/code_compile'

			path_to_question = BASE_DIR + '/Contest/%s'%contest.Name + '/%s'%question.Name

			if not os.path.exists(dir_path):
				os.makedirs(dir_path, 0o777)
			nam = request.user
			compile_folder_path = BASE_DIR + '/Contest/%s'%contest.Name + '/%s'%question.Name +'/code_compile/%s'%nam + '%s'%p
			if not os.path.exists(compile_folder_path):
				os.makedirs(compile_folder_path, 0o777)

			if code.language=='c++' or code.language=='C++':
				file2write=open(compile_folder_path + '/%s'%nam + '%s'%p + '.cpp','w')
				file2write.write(code.code)
				file2write.close()
				file_path = compile_folder_path +'/%s'%nam + '%s'%p + '.cpp'
			elif code.language=='python2' or code.language=='Python2' or code.language=='python3' or code.language=='Python3':
				file2write=open(compile_folder_path + '/%s'%nam + '%s'%p + '.py','w')
				file2write.write(code.code)
				file2write.close()
				file_path = compile_folder_path +'/%s'%nam + '%s'%p + '.py'
			elif code.language=='C' or code.language=='c':
				file2write=open(compile_folder_path + '/%s'%nam + '%s'%p + '.c','w')
				file2write.write(code.code)
				file2write.close()
				file_path = compile_folder_path +'/%s'%nam + '%s'%p + '.c'

			
			if code.language=='c++' or code.language=='C++' or code.language=='C' or code.language=='c'  or code.language=='C++ 14' or code.language=='c++ 14':
				compile_folder_path_input = compile_folder_path + '/Input'
				if not os.path.exists(compile_folder_path_input):
					os.makedirs(compile_folder_path_input, 0o777)

				compile_folder_path_output = compile_folder_path + '/Output'
				if not os.path.exists(compile_folder_path_output):
					os.makedirs(compile_folder_path_output, 0o777)
				#cmd = 'g++ %s'%file_path +" -o "+ compile_folder_path +'/%s'%nam + '%s'%p + '.out'
				temp_out =  compile_folder_path +'/%s'%nam + '%s'%p + '.out'
				if code.language=='C' or code.language=='c':
					cmd = ['gcc',file_path,"-o",temp_out]
				else:	
					cmd = ['g++','-std=c++14',file_path,"-o",temp_out]

				path_to_send = compile_folder_path +'/%s'%nam + '%s'%p + '.out'
				try:
					status = subprocess.run(cmd, timeout=2.1)
					if status.returncode==0:
						print("Running Successfully")
						ans =0	
						ans =	generate_input_contest(path_to_send,contest,question,path_to_question,compile_folder_path)
						print("paras",ans)
						if ans==0:
							return HttpResponse("WA")
						elif ans!=1:
							return HttpResponse("TLE")	
						else:
							print(datetime.now() - startTime)
							user = request.user
							end_time = datetime.now();
							Submit_Question.objects.create(user=user,contest=contest,question=question,verdict=1,start_time = startTime,end_time=datetime.now())
							# score,created = User_score.objects.get_or_create(user=request.user)
							# if created:
							# timee=end_time-startTime
							# print(('%02d:%02d.%d'%(timee.days,timee.seconds,timee.microseconds))[:-4])
							# if(end_time-startTime > 0:01:00.000000):
							# 	return HttpResponse("TLE",end_time-startTime)

							return HttpResponse("AC",datetime.now() - startTime)
					else:
						print("Compilation Error")
						return HttpResponse("Compilation Error")
							
					
				except subprocess.TimeoutExpired:
					print('Timeout')
					return HttpResponse("TLE Timeout",datetime.now() - startTime)	
			
			elif code.language=='python2' or code.language=='Python2' or code.language=='python3' or code.language=='Python3':
				compile_folder_path_input = compile_folder_path + '/Input'
				if not os.path.exists(compile_folder_path_input):
					os.makedirs(compile_folder_path_input, 0o777)

				compile_folder_path_output = compile_folder_path + '/Output'
				if not os.path.exists(compile_folder_path_output):
					os.makedirs(compile_folder_path_output, 0o777)
				path_to_send  = file_path	
				#cmd = 'g++ %s'%file_path +" -o "+ compile_folder_path +'/%s'%nam + '%s'%p + '.out'
				print(path_to_send,contest,question,path_to_question,compile_folder_path)
				ans =	python_run(path_to_send,contest,question,path_to_question,compile_folder_path,code.language)
				print("paras",ans)
				if ans==0:
					return HttpResponse("WA")
				elif ans!=1:
					return HttpResponse("TLE")	
				else:
					print(datetime.now() - startTime)
					user = request.user
					end_time = datetime.now();
					Submit_Question.objects.create(user=user,contest=contest,question=question,verdict=1,start_time = startTime,end_time=datetime.now())
					
					return HttpResponse("AC",datetime.now() - startTime)
					
			else:	
				return HttpResponse("Language Not Supported")

				


	else:
		form = NewTopicForm3()
	return render(request, 'code_snippet.html', {'form' : form})	#submit solution in contest

def generate_input_contest(path_to_send,contest,question,path_to_question,compile_folder_path):
	startTime = datetime.now()
	testcase = Testcase.objects.filter(contest=contest,question=question)
	
	ans =0
	for testcase in testcase:
		print(testcase.inpt)
		name_out = testcase.outp.split('/')[-1]
		#cmd = '/home/paras/Desktop/coding/my-project/Judge/Contest/Algofuzz18.1/Divisor4/code_compile/demo78/demo78.out < /home/paras/Desktop/coding/my-project/Judge/Contest/Algofuzz18.1/Divisor4/testcases/Input/i18.txt > result.txt'
		#cmd = '%s'%path_to_send + ' < ' '%s'%BASE_DIR + '%s'%testcase.inpt + ' > ' + '%s'%compile_folder_path + '/Output/%s'%name_out #running a c++ program(name of file)
		temp_out = '%s'%compile_folder_path + '/Output/%s'%name_out
		temp_out2 = '%s'%BASE_DIR + '%s'%testcase.inpt
		myinput = open(temp_out2)
		myoutput = open(temp_out,"w")
		cmd = [path_to_send ]
		print("hi",cmd,"hi")
		out_testcase = '%s'%BASE_DIR + '%s'%testcase.outp 
		compile_testcase = '%s'%compile_folder_path + '/Output/%s'%name_out
	#	print("this",out_testcase,compile_testcase)

		try:
			p = subprocess.run(cmd,timeout=1,stdin=myinput,stdout = myoutput)
			if p.returncode==0:
				print("Successfully Compiled")
				ans = match_testcase_contest(out_testcase,compile_testcase,ans)
				if ans==0:
					break
			else:
				print("Error")
				ans=0
				break
		except subprocess.TimeoutExpired:
			print('Timeout',"hi")
			return HttpResponse("TLE Timeout",datetime.now() - startTime)
	if ans==0:
		return ans
	else:
		return ans	



def match_testcase_contest(output_path,compile_path,ans):
	cmd = "diff -w %s"%output_path + " %s"%compile_path
	try:
		p = subprocess.call(cmd,shell=True)
	except subprocess.TimeoutExpired(timeout=61):
		print("hi")	
	if p==0:
		ans=1
		return ans
	else:
		ans=0
		print("Error")
		return ans


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


def ranking(request,pk):
	submission = Submit_Question.objects.filter(contest=pk,verdict=1).order_by('time')
	print(submission)
	return render(request,'ranking.html',{'submission':submission})


def python_run(path_to_send,contest,question,path_to_question,compile_folder_path,code_language):
	startTime = datetime.now()
	testcase = Testcase.objects.filter(contest=contest,question=question)
	ans =0
	for testcase in testcase:
		print("gggg")
		name_out = testcase.outp.split('/')[-1]
		temp_out = '%s'%compile_folder_path + '/Output/%s'%name_out
		temp_out2 = '%s'%BASE_DIR + '%s'%testcase.inpt
		myinput = open(temp_out2)
		myoutput = open(temp_out,"w")
		if code_language=='python2' or code_language=='Python2':
			cmd = ["python2",path_to_send]
		else:
			cmd = ["python3",path_to_send]
		out_testcase = '%s'%BASE_DIR + '%s'%testcase.outp 
		compile_testcase = '%s'%compile_folder_path + '/Output/%s'%name_out
	#	print("this",out_testcase,compile_testcase)

		try:
			p = subprocess.run(cmd,timeout=5.5,stdin=myinput,stdout = myoutput)
			if p.returncode==0:
				print("Successfully Compiled")
				ans = match_testcase_contest(out_testcase,compile_testcase,ans)
				if ans==0:
					break
			else:
				print("Error")
				ans=0
				break
		except subprocess.TimeoutExpired:
			print('Timeout',"hi")
			return HttpResponse("TLE Timeout",datetime.now() - startTime)
	if ans==0:
		return ans
	else:
		return ans	

#check whether code is safe to run
def is_safe(input_check, language):
    input_check = input_check.lower()

    if 'python3' in lang or 'python2' in lang or 'Python3' in lang or 'Python3' in lang:
        if 'import os' in input_check or 'system(' in input_check or 'popen' in input_check or 'subprocess' in input_check:
            return False
        else:
            return True
    elif lang == 'java' or lang == 'Java':
        if '.getruntime(' in input_check or 'processbuilder(' in input_check:
            return False
        else:
            return True
    elif 'subprocess' in input_check or'fopen(' in input_check or 'open(' in input_check :
        return False
    return True