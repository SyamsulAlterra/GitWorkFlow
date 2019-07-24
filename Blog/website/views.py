from django.shortcuts import render

# Create your views here.
def author_view(request):
    return render(request,'author.html',{})

def home(request):
    return render(request, 'home.html', {})