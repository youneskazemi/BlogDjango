from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(label="یوزرنیم", max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label="پسورد", max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label="یوزرنیم", max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(label="ایمیل", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(label="پسورد", max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="تایید پسورد", max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     user = User.objects.filter(email=email)
    #     if user.exists():
    #         raise forms.ValidationError("ایمیل تکراری میباشد!")
    #     return email
    #
    # def clean_password2(self):
    #     password1 = self.cleaned_data['password1']
    #     password2 = self.cleaned_data['password2']
    #     if password1 != password2:
    #         raise forms.ValidationError("پسوردها یکسان نمیباشد!")
    #     return password2

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')
        if p1 != p2:
            raise forms.ValidationError("پسوردها یکسان نمیباشد!")
        email = cleaned_data.get('email')
        user = User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError("ایمیل تکراری میباشد!")
        user = cleaned_data.get('username')
        user = User.objects.filter(username=user)
        if user.exists():
            raise forms.ValidationError("یوزرنیم تکراری میباشد!")











