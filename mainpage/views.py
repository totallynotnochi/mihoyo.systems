# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from mainpage.uidFORM import GenshinUidForm
from django.shortcuts import render, redirect
from mainpage.APIGetter import api_getter
import asyncio


def mainpagereturn(request):
    return render(request, 'index.html')


def optimizerreturn(request):
    return render(request, 'generic.html')


def genshin_uid_input(request):
    if request.method == 'POST':
        print("POST SUBMITTED")
        form = GenshinUidForm(request.POST)
        if form.is_valid():
            print("POST IS VALID (UID)")
            uid = form.cleaned_data['GenshinUID']
            request.session['uid'] = uid  # Store UID in session
            return redirect('uid_loaded_index')  # Redirect to new page
    else:
        form = GenshinUidForm()
    return render(request, 'index.html', {'form': form})


def uid_loaded_index(request):
    uid = request.session.get('uid', None)
    if uid:
        genshin_data = asyncio.run(api_getter(uid))  # Fetch data from the API

        if genshin_data:  # Check if data was fetched successfully
            return render(request, 'UIDLoadedIndex.html', {'genshin_data': genshin_data})
        else:
            return  render(request, 'UIDLoadedIndex.html', {'error_message': 'Error fetching data from API'})
    else:
        return render(request, 'UIDLoadedIndex.html', {'error_message': 'UID not found'})


def HTMLdevreturn(request):
    return render(request, 'am studying.html')

# Create your views here.
