from django.shortcuts import render
from uidFORM import MyForm  # Import your form class
def user_input(request):
    if request.method == 'POST':
        form = MyForm(request.POST)  # Create form instance with submitted data
        GenshinUID = form.cleaned_data['UID']