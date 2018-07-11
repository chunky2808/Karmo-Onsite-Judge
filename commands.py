from subprocess import Popen, PIPE
import subprocess


'''
working compilation
'''
# cmd = 'g++'
# cmd2= '/home/paras/Desktop/coding/my-project/Judge/working_input.cpp'
# cmd3 = './a.out'
# out =open("/home/paras/Desktop/coding/my-project/Judge/out04.txt","wb")
# process = Popen([cmd3], stdout=out, stderr=PIPE)
# try:
# 	stdout, stderr = process.communicate(timeout=1)
# 	print(stderr)
# except subprocess.CalledProcessError as e:
# 	print(e)
# 	print(process.returncode)

# print(process.returncode)

myinput = open('/home/paras/Desktop/coding/my-project/Judge/Contest/Algofuzz18.1/Divisor4/testcases/Input/i19.txt')
myoutput = open('/home/paras/Desktop/coding/my-project/Judge/Contest/Algofuzz18.1/Divisor4/code_compile/demo171/Output/o19.txt', 'w')
#cmd = ['g++','/home/paras/Desktop/coding/my-project/Judge/working_input.cpp','-o','a.out']
#cmd = ['/home/paras/Desktop/coding/my-project/Judge/Contest/Algofuzz18.1/Divisor4/code_compile/demo171/demo171.out', '<', '/home/paras/Desktop/coding/my-project/Judge/Contest/Algofuzz18.1/Divisor4/testcases/Input/i19.txt', '>', '/home/paras/Desktop/coding/my-project/Judge/Contest/Algofuzz18.1/Divisor4/code_compile/demo171/Output/o19.txt']

cmd = ['/home/paras/Desktop/coding/my-project/Judge/Contest/Algofuzz18.1/Divisor4/code_compile/demo171/demo171.out']

#cmd = ['./a.out']

try:
	p = subprocess.run(cmd, timeout=2,stdin=myinput,stdout=myoutput)
	print(p)	
except subprocess.TimeoutExpired:
	print('process ran too long')




'''
working compilation
'''



'''
working matching and output
'''


# cmd = 'g++'
# cmd2= '/home/paras/Desktop/coding/my-project/Judge/Contest/Algofuzz18.1/Divisor4/solution/Solution.cpp'
# cmd3 = './a.out'
# cmd4 = '/home/paras/Desktop/coding/my-project/Judge/Contest/Algofuzz18.1/Divisor4/testcases/Input/i19.txt'
# out =open("/home/paras/Desktop/coding/my-project/Judge/out04.txt","wb")
# #process = Popen([cmd,cmd2], stdout=out, stderr=PIPE)
# process = Popen([cmd3,'<',cmd4], stdout=PIPE, stderr=PIPE)
# try:
# 	stdout, stderr = process.communicate()
# 	print(stderr,stdout)
# except:
# 	print(process.returncode,"hi")



'''
working matching and output
'''
