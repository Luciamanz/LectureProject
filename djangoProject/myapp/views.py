from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from datetime import datetime
from . import utils, models
from django.http import HttpResponseRedirect
from django.urls import reverse


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


def register(request):
    context = dict()
    form = UserCreationForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        dob = request.POST["dob"]
        acct_holder = models.AccountHolder(
            user=new_user,
            date_of_birth=dob,
        )
        acct_holder.save()
        return HttpResponseRedirect(reverse('home'))
    else:
        context['form'] = UserCreationForm()
        return render(
            request,
            "myapp/register.html",
            context,
        )
