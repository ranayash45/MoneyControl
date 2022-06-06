from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Expense
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
# Create your views here.
from django.views import generic

class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "expense_list"
    def get_queryset(self):
        return Expense.objects.all()

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