from django.urls import path
from . import views

app_name="money"
urlpatterns=[
    path("",views.IndexView.as_view()),
    path("list/",views.IndexView.as_view(),name="list"),
    path("details/<int:expense_id>",views.DetailView.as_view()),
    path("users/",views.users),
    path("add/",views.AddExpense,name='add'),
    path("update/<int:expense_id>",views.UpdateExpense,name='update'),
    path("update/",views.UpdateExpense,name='update'),
    path("delete/<int:expense_id>",views.deleteExpense,name='delete')
]
