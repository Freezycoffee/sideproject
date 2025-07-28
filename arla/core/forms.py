from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, help_text='Required', widget=forms.TextInput(attrs={'placeholder': 'Input Your Username', 'class': 'mb-5 w-full py-4 px-6 border border-black shadow-[5px_5px_0px_0px_rgba(0,0,0)] rounded-xl'}))

    password = forms.CharField(max_length=100, help_text='Required', widget=forms.PasswordInput(attrs={'placeholder': 'Input Your Password', 'class': 'mb-5 w-full py-4 px-6 border border-black shadow-[5px_5px_0px_0px_rgba(0,0,0)] rounded-xl'}))


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required', widget=forms.TextInput(attrs={'placeholder': 'Input Your Email', 'class': 'mb-5 w-full py-4 px-6 border border-blue-700 shadow-[5px_5px_0px_0px_rgba(29,78,216)] rounded-xl'}))

    first_name = forms.CharField(max_length=50, help_text='Required', widget=forms.TextInput(attrs={'placeholder': 'Input Your First Name', 'class': 'sm:w-4/5 w-full mb-5 py-4 px-6 border border-blue-700 shadow-[5px_5px_0px_0px_rgba(29,78,216)] rounded-xl'}))

    last_name = forms.CharField(max_length=50, help_text='Required', widget=forms.TextInput(attrs={'placeholder': 'Input Your Last Name', 'class': 'sm:w-4/5 w-full mb-5 py-4 px-6 border border-blue-700 shadow-[5px_5px_0px_0px_rgba(29,78,216)] rounded-xl'}))

    username = forms.CharField(max_length=50, help_text='Required', widget=forms.TextInput(attrs={'placeholder': 'Input Your Username', 'class': 'mb-5 w-full py-4 px-6 border border-blue-700 shadow-[5px_5px_0px_0px_rgba(29,78,216)] rounded-xl'}))

    password1 = forms.CharField(max_length=100, help_text='Required', widget=forms.PasswordInput(attrs={'placeholder': 'Input Your Password', 'class': 'mb-5 w-full py-4 px-6 border border-blue-700 shadow-[5px_5px_0px_0px_rgba(29,78,216)] rounded-xl'}))

    password2 = forms.CharField(max_length=100, help_text='Required', widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Your Password', 'class': 'mb-5 w-full py-4 px-6 border border-blue-700 shadow-[5px_5px_0px_0px_rgba(29,78,216)] rounded-xl'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class updateProfileForm(UserChangeForm):
    password = None  # Disable password field in the form
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Input Your Email', 'class': 'mb-2 w-full py-2 px-3 mt-1 border border-blue-700 shadow-[5px_5px_0px_0px_rgba(29,78,216)] rounded-xl'}))

    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Input Your First Name', 'class': 'mb-2 w-full py-2 px-3 mt-1 border border-blue-700 shadow-[5px_5px_0px_0px_rgba(29,78,216)] rounded-xl'}))

    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Input Your Last Name', 'class': 'mb-2 w-full py-2 px-3 mt-1 border border-blue-700 shadow-[5px_5px_0px_0px_rgba(29,78,216)] rounded-xl'}))

    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Input Your Username', 'class': 'mb-2 w-full py-2 px-3 mt-1 border border-blue-700 shadow-[5px_5px_0px_0px_rgba(29,78,216)] rounded-xl'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', )

class PasswordChangeForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=100,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Input Your New Password', 'class': 'mb-5 w-full py-2 px-3 border border-black shadow-[2px_2px_0px_0px_rgba(0,0,0)] rounded-xl'}))

    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Your New Password', 'class': 'mb-5 w-full py-2 px-3 border border-black shadow-[2px_2px_0px_0px_rgba(0,0,0)] rounded-xl'}))

    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')