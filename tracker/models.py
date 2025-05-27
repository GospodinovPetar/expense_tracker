from decimal import Decimal

from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


# Create your models here.


class Income(models.Model):
    income_id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=100)  # E.g., "Salary", "Bonus"
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))]
    )
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.source}: ${self.amount} on {self.date}"


class Expenses(models.Model):
    categories = [
        ("Healthcare", "Healthcare"),
        ("Education", "Education"),
        ("Entertainment", "Entertainment"),
        ("Utilities", "Utilities"),
        ("Groceries", "Groceries"),
        ("Memberships", "Memberships"),
        ("Debt", "Debt"),
        ("Emergency Fund", "Emergency Fund"),
        ("Other", "Other"),
    ]

    expense_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    expense = models.IntegerField(validators=[MinValueValidator(1, "Invalid value")])
    date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=50, choices=categories)
