from django import forms

class MyForm(forms.Form):
    GenshinUID = forms.CharField(label="Your UID")