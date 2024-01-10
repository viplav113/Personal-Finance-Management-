from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=140, verbose_name='Name of the Expense Request', default='')
    date_of_expense = models.DateField(default=timezone.now)
    
    CATEGORY_CHOICES = [
        ('Health', 'Health'),
        ('Electronics', 'Electronics'),
        ('Travel', 'Travel'),
        ('Education', 'Education'),
        ('Books', 'Books'),
        ('Others', 'Others'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "\n" + self.description
