from django import forms
class Userinfoform(forms.Form):
    name = forms.CharField(label='Your Name', max_length=10)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField( max_length=100)