from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.phone_number})"

class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='loans')
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.FloatField(help_text="In percentage, e.g., 12.5")
    repayment = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    date = models.DateField()

    @property
    def balance(self):
        return self.loan_amount - self.repayment

    def __str__(self):
        return f"Loan #{self.id} for {self.customer.name} {self.loan_amount}"

class Interest(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='interest_payments')
    date = models.DateField()
    interest_amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Interest paid on {self.date} for Loan #{self.loan.id}"

