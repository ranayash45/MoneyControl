from cmath import exp
from datetime import datetime
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Expense
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
# Create your views here.
from django.views import generic

class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "expense"
    def get_queryset(self):
        expense = {
            "list":[],
            "total":0
        }
        total = 0
        expense_list = Expense.objects.all()
        for item in expense_list:
            total += item.expenseValue
        expense["list"] = expense_list
        expense["total"] = total
        return expense

class DetailView(generic.DetailView):
    template_name = "detail.html"
    model = Expense

class ResultView(generic.DetailView):
    template_name = "detail.html"
    model = Expense

def AddExpense(request):
    if request.method == "POST":
        expenseName = request.POST["expenseName"]
        expenseCost = request.POST["expenseCost"]
        e = Expense(expenseName=expenseName,expenseValue=expenseCost,expenseDate=timezone.now())
        e.save()
        return HttpResponseRedirect("/money/list")
    return render(request,"add.html")

def users(request):
    return HttpResponse("Total Users")

def deleteExpense(request,expense_id):
    expense = get_object_or_404(Expense,pk=expense_id)
    expense.delete()
    return HttpResponseRedirect("/money/list")

def UpdateExpense(request,expense_id=""):
    if request.method == "POST":
        expense_id = request.POST["expense_id"]
        expense_name = request.POST["expenseName"]
        expense_value = request.POST["expenseValue"]
        expense = get_object_or_404(Expense,pk=expense_id)
        expense.expenseName = expense_name
        expense.expenseValue = expense_value
        expense.save()
        return HttpResponseRedirect("/money/list")
    else:
        expense = get_object_or_404(Expense,pk=expense_id)
        context = {
            'expense':expense
        }
        return render(request,'update.html',context)