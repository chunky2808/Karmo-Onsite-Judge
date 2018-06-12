from django.contrib import admin
from .models import Contest,Question,Code_Snippet,Testcase

admin.site.register(Contest)
admin.site.register(Question)
admin.site.register(Code_Snippet)
admin.site.register(Testcase)
# Register your models here.
