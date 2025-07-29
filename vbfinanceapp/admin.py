from django.contrib import admin
from .models import Customer, Loan, Interest

admin.site.register(Customer)
admin.site.register(Loan)
admin.site.register(Interest)

