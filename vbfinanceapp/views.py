from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Loan, Interest
from .forms import CustomerForm, LoanForm, InterestForm

# ========== CUSTOMER VIEWS ==========
from django.db.models import Q

def homepage(request):
    query = request.GET.get('q')
    customers = Customer.objects.all()

    if query:
        customers = customers.filter(name__icontains=query)

    return render(request, 'homepage.html', {'customers': customers, 'query': query})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})

def customer_detail(request, name):
    customer = get_object_or_404(Customer, name=name)
    loans = customer.loans.all()
    return render(request, 'customer_detail.html', {'customer': customer, 'loans': loans})


# ========== LOAN VIEWS ==========

def loan_list(request):
    loans = Loan.objects.all()
    return render(request, 'loan_list.html', {'loans': loans})

def add_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = LoanForm()
    return render(request, 'add_loan.html', {'form': form})

from django.db.models import Sum

def loan_detail(request, name):
    customer = get_object_or_404(Customer, name=name)
    loans = Loan.objects.filter(customer=customer)

    # Total repaid and interest collected
    total_repayment = loans.aggregate(Sum('repayment'))['repayment__sum'] or 0
    total_interest = Interest.objects.filter(loan__in=loans).aggregate(Sum('interest_amount_paid'))['interest_amount_paid__sum'] or 0

    return render(request, 'loan_detail.html', {
        'customer': customer,
        'loans': loans,
        'total_repayment': total_repayment,
        'total_interest': total_interest,
    })



# ========== INTEREST VIEWS ==========

def interest_list(request):
    interests = Interest.objects.all()
    return render(request, 'interest_list.html', {'interests': interests})

def add_interest(request):
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = InterestForm()
    return render(request, 'add_interest.html', {'form': form})

def interest_detail(request, name):
    customer = get_object_or_404(Customer, name=name)
    loans = customer.loans.prefetch_related('interest_payments')
    
    all_interests = []
    for loan in loans:
        all_interests.extend(loan.interest_payments.all())

    return render(request, 'interest_detail.html', {
        'customer': customer,
        'interest_payments': all_interests
    })
    
from .forms import RepaymentForm

def repayment_view(request, customer_name):
    customer = get_object_or_404(Customer, name=customer_name)
    loan = Loan.objects.filter(customer=customer).order_by('-id').first()


    if request.method == 'POST':
        form = RepaymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            loan.repayment += amount
            #loan.balance = loan.loan_amount - loan.repayment
            loan.save()
            return redirect('homepage')
    else:
        form = RepaymentForm()

    return render(request, 'repayment.html', {'form': form, 'customer': customer,'loan':loan})

  