__author__ = 'dl'

from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login,logout as django_logout
from django.contrib.auth.decorators import login_required

@login_required
def test1(request):
    return render_to_response('test/test1.html',{'msg':'test1','islogin':request.session['islogin']})


@login_required
def test2(request):
    return render_to_response('test/test1.html',{'msg':'test2'})


def login(request):
    username=request.GET.get('username','')
    password=request.GET.get('password','')
    user=authenticate(username=username,password=password)
    print request
    if user :
        django_login(request,user)
        request.session['islogin']=1;
        return redirect(request.path)
    if (username==''):
        return render_to_response('test/login.html')
    return render_to_response('test/login.html',{'msg':'error in auth'})

def logout(request):
    django_logout(request)
    return test2(request)