from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.views import generic
from account.models import *
from datetime import date,datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from account.forms import *
from django.contrib.auth import logout,authenticate,login
def index(request):
    return render(
        request,'index.html'
    )
@login_required
def search(request):
    if not request.user.is_superuser:
        return HttpResponse("<h1>Permission denied!!</h1>")
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            department=form.cleaned_data['department']
            number=request.POST.get('amount')
            number=int(number)
            lectures_list = Lecturers.objects.filter(department = department)
            for i in lectures_list:
                i.savings+=number
                i.save()
            context = {
            'lectures_list':lectures_list,
            'form': form
            }
        return render(request, 'search.html', context)  
    else:
        form = SearchForm()
        lectures_list = Lecturers.objects.all() 
           
    context = {
            'lectures_list':lectures_list,
            'form': form
            }

    return render(request, 'search.html', context)
    
def success(request):
    return render(request, 'success.html')

@login_required
def details(request):
    if not request.user.is_superuser:
        return HttpResponse("<h1>Permission denied!!</h1>")
    detail_list = Lecturers.objects.all()
    context = {
    'detail_list': detail_list
    }
    print(detail_list)
    return render(request,'details.html',context)
@login_required
def total(request):
    if not request.user.is_superuser:
        return HttpResponse("<h1>Permission denied!!</h1>")
    total_list = Lecturers.objects.all()
    total_amount=0
    context={}
    context['CS']=0
    context['IS']=0
    context['EC']=0
    context['Civil']=0
    context['NTD']=0
    context['MECH']=0
    context['MATHS']=0
    context['PHYSICS']=0
    context['CHEMISTRY']=0
    context['LIBRARY']=0
    for i in total_list:
        context[i.department]+=i.savings
        total_amount+=i.savings
    context['total']=total_amount
    return render(request,'total.html',context)
@login_required
def loan_form(request,name,dept):
    if not request.user.is_superuser:
        return HttpResponse("<h1>Permission denied!!</h1>")
    context={
        "name":name,
        "dept":dept
    }
    if dept=="NTD":
        context['loan']=50000
    else:
        context['loan']=100000
    return render(request,'loan_form.html',context)
@login_required
def take_loan(request):
    if not request.user.is_superuser:
        return HttpResponse("<h1>Permission denied!!</h1>")
    if request.method=='POST':
        name=request.POST.get('name')
        dept=request.POST.get('dept')
        loan=request.POST.get('loan')
        user_obj=User.objects.get(username=name)
        lec_obj=Lecturers.objects.get(username=user_obj)
        lec_obj.loan_balance=0
        lec_obj.loan_left=int(loan)
        lec_obj.save()
    return HttpResponseRedirect(reverse('details'))
@login_required
def update_form(request,name,dept):
    if not request.user.is_superuser:
        return HttpResponse("<h1>Permission denied!!</h1>")
    context={
        "name":name,
        "dept":dept
    }
    if dept=="NTD":
        context['emi']=2292
    else:
        context['emi']=4584
    return render(request,'update_form.html',context)
@login_required
def update_loan(request):
    if not request.user.is_superuser:
        return HttpResponse("<h1>Permission denied!!</h1>")
    if request.method=='POST':
        name=request.POST.get('name')
        dept=request.POST.get('dept')
        emi=request.POST.get('emi')
        user_obj=User.objects.get(username=name)
        lec_obj=Lecturers.objects.get(username=user_obj)
        lec_obj.emi+=int(emi)
        if dept=="NTD":
            lec_obj.loan_left-=2083
            if lec_obj.emi==2292*24:
                lec_obj.loan_balance=50000
                lec_obj.loan_left=0
                lec_obj.emi=0
        else:
            lec_obj.loan_left-=4166
            if lec_obj.emi==4584*24:
                lec_obj.loan_balance=100000
                lec_obj.loan_left=0
                lec_obj.emi=0
        lec_obj.save()
        hist=History(username=lec_obj,hemi=lec_obj.emi,loan_left=lec_obj.loan_left,date=datetime.datetime.now())
        hist.save()
    return HttpResponseRedirect(reverse('details'))
@login_required
def history(request,name):
    user_obj=User.objects.get(username=name)
    lec_obj=Lecturers.objects.get(username=user_obj)
    history_list=History.objects.filter(username=lec_obj)
    context={
        "history_list":history_list
    }
    return render(request,'history.html',context)
@login_required
def history_user(request):
    lec_obj=Lecturers.objects.get(username=request.user)
    history_list=History.objects.filter(username=lec_obj)
    context={
        "history_list":history_list
    }
    return render(request,'history.html',context)
@login_required
def user_details(request):
    file=Lecturers.objects.get(username=request.user)
    context={
        "file":file
    }
    return render(request,'user_detail.html',context)




# Create your views here.

# Create your views here.
