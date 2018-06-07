from django.shortcuts import render
import subprocess
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.contrib.auth import login as auth_login

import os 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

from django.contrib.auth.forms import UserCreationForm

def signup(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request, user)
			return redirect('home')
	else:	
		form = UserCreationForm()
	return render(request,'users/signup.html',{'form':form})