# Karmo-Onsite-Judge
It is an onsite judge made on likes of SPOJ and Codechef without using any internet connection.

It will allow colleges with poor internet connection to host coding competition in college.

It is an web app which runs on college intranet connection which makes it cross-platform.

Improved from the existing system of PC2.

It is designed to meet the requirement specific to contests hosted at JIIT, Noida but most of its components can be easily changed to meet requirement of any other college.

The only constraint is that it requires Linux to run the Judge, while submission can be made from any operating system.

The Judge currently accepts submission in following languages:
1) C
2) C++,C++14
3) Python 2,Python 3
4) Java, Java 8

# Features

1) Currently,the judge allows user to compile and test code in different languages,submit questions in different languages,
  create contest,delete contest,view ranklist.
  
2) Added Bug-checker to check for malicious code/virus.

3) Provides three categories- User,Coordinator,Admin.

User-can view contests,submit question on contest,compile and test,view ranklist.

Coordinator- can add problem for particular contest with testcase and solution.

Admin - can create,delete contest,user account and questions.

# To run

1) Clone the project

2) run python manage.py makemigrations

3) run python manage.py migrate

4) run python manage.py runserver to run the web app.
