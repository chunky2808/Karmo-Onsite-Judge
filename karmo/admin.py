from django.contrib import admin
from .models import Contest,Question,Code_Snippet,Testcase,Submit_Question

admin.site.register(Contest)
admin.site.register(Question)
admin.site.register(Code_Snippet)
admin.site.register(Testcase)
admin.site.register(Submit_Question)
