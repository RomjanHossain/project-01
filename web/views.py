from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def gallery(request):
    search = request.POST.get('get_search')
    stuff_for_frontend = {
        'get_search': search,
    }
    return render(request, 'gallery/index.html', stuff_for_frontend)
