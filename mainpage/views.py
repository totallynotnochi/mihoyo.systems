# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from mainpage.uidFORM import GenshinUidForm
from django.shortcuts import render, redirect

def mainpagereturn(request):
    return render(request, 'index.html')

def optimizerreturn(request):
    return render(request, 'generic.html')

def genshin_uid_input(request):
    if request.method == 'POST':
        print("POST SUCCESSS")
        form = GenshinUidForm(request.POST)
        if form.is_valid():
            print("POST IS VALID?!?!!?")
            uid = form.cleaned_data['GenshinUID']
            request.session['uid'] = uid # Store UID in session
            return redirect('uid_loaded_index')  # Redirect to new page
    else:
        form = GenshinUidForm()
    return render(request, 'index.html', {'form': form})

def uid_loaded_index(request):
    print("test")
    uid = request.session.get('uid', None) # Retrieve UID from session
    return render(request, 'UIDLoadedIndex.html', {'uid': uid})


def HTMLdevreturn(request):
    return render(request, 'am studying.html')



# Create your views here.