from django import forms
from .models import Customer, Loan, Interest

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone_number', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['customer', 'loan_amount', 'interest_rate', 'repayment', 'date']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'loan_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'interest_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'repayment': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['loan', 'date', 'interest_amount_paid']
        widgets = {
            'loan': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'interest_amount_paid': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class RepaymentForm(forms.Form):
    amount = forms.DecimalField(label="Repayment Amount", max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
