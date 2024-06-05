# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from mainpage.uidFORM import GenshinUidForm

def mainpagereturn(request):
    return render(request, 'index.html')

def optimizerreturn(request):
    return render(request, 'generic.html')

def genshin_uid_input(request):
    if request.method == 'POST':
        form = GenshinUidForm(request.POST)
        if form.is_valid():
            genshin_uid = form.cleaned_data['GenshinUID']
            # Process the 'genshin_uid'
            return HttpResponse("Success")
        else:
            error_message = "Invalid UID. Please enter a valid number."
            return HttpResponse(error_message)
    else:
        form = GenshinUidForm()
    return render(request, 'index.html', {'form': form})



# Create your views here.