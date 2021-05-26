from django.shortcuts import render
from django.contrib import admin
from basic_app.forms import userform,userinfoform

from django.contrib.auth import authenticate,login,logout
from django.http  import HttpResponseRedirect, HttpResponse
#from django.core.urlresolvers import reverse
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,"index.html")

@login_required
def special(request):
    return HttpResponse(' ur in login')



@login_required
def user_logout(request):
    return HttpResponseRedirect(reverse,'index')




def register (request):
    registered = False
    if request.method=='POST':
        user_form=userform(data=request.POST)
        user_info_form=userinfoform(data=request.POST)
        if user_form.is_valid() and user_info_form.is_valid():

            User=user_form.save()
            User.set_password(User.password)
            User.save()

            profile=user_info_form.save(commit=False)
            profile.User =User

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print(user_form.errors,user_info_form.errors)

    else:
        user_form=userform
        user_info_form =userinfoform
    return render(request,"registartion.html",{'user_form':user_form ,'user_info_form':user_info_form,'registered':registered})

def user_login(request):
    if request.method == 'post':


        username=request.POST.get('username')
        password=request.POST.grt('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponceRedirect(reverse('index'))
            else:
                return HttpResponce('ACCOUNT NOT ACTIVE')
        else:
            print('wrong longin')
            print('username: {} and password: {})'.format(username,password))
            return HttpResponce("invalid details")
    else:
        return render(request,'log_in.html',{})
