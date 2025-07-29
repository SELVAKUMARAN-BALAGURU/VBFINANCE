from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),

    # Customer
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('customers/<str:name>/', views.customer_detail, name='customer_detail'),
    path('repayment/<str:customer_name>/', views.repayment_view, name='repayment'),
    
    # Loan
    path('loans/', views.loan_list, name='loan_list'),
    path('loans/add/', views.add_loan, name='add_loan'),
    path('loans/<str:name>/', views.loan_detail, name='loan_detail'),

    # Interest
    path('interests/', views.interest_list, name='interest_list'),
    path('add-interest/', views.add_interest, name='add_interest'),
    path('interests/<str:name>/', views.interest_detail, name='interest_detail'),
]
