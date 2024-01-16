from django.shortcuts import render

from datetime import datetime


# Create your views here.

def home(request):
    cur_time = datetime.now()
    context = {'time': cur_time}
    return render(request, template_name='myapp/homepage.html',context=context)

