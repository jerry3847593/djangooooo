from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = {'name', 'age', 'major', 'grade', 'hometown'}