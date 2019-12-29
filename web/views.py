from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def gallery(request):
    search = request.POST.get('get_search')
    print(search)
    return render(request, 'gallery/index.html')
