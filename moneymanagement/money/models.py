from operator import truediv
from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField('UserID',primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_date = models.DateTimeField('Date and Time when user is created')

class Expense(models.Model):
    expenseName = models.CharField(max_length=255)
    expenseValue = models.FloatField('Expense of User')
    expenseDate = models.DateTimeField('Date and Time when expense Done')
    def __str__(self):
        return self.expenseName+" => "+str(self.expenseValue)