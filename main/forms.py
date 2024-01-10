from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Health', 'Health'),
        ('Electronics', 'Electronics'),
        ('Travel', 'Travel'),
        ('Education', 'Education'),
        ('Books', 'Books'),
        ('Others', 'Others'),
    ]

    name = forms.CharField(max_length=140, label='Name of the Expense Request')
    date_of_expense = forms.DateField(label='Date of Expense')
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    description = forms.CharField(widget=forms.Textarea)
    amount = forms.DecimalField(label='Amount', min_value=0)

    class Meta:
        model = Post
        fields = ["name", "date_of_expense", "category", "description", "amount"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.author = self.instance.author
            instance.save()
        return instance

