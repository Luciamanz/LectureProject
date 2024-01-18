from django.shortcuts import render

from datetime import datetime

from . import utils


# Create your views here.

def home(request):
    cur_time = datetime.now()
    context = {'time': cur_time}
    return render(request, template_name='myapp/homepage.html', context=context)


def maintenance(request):
    if request.method == "POST":
        if request.POST["selection"] == "currencies":
            print("call my post_currencies method")
            currencies = utils.get_currencies()
            utils.add_currencies_to_db(currencies)
        elif request.POST["selection"] == "rates":
            print("call my post_rates method")
    return render(request, template_name='myapp/maintenance.html', context={})
