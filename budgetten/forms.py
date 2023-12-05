# budgetten/forms.py

# django
from django import forms

# Expense form
class ExpenseForm(forms.Form):
  title    = forms.CharField()
  amount   = forms.IntegerField()
  category = forms.CharField()