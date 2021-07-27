from django.shortcuts import render

def index(request):

    return render(request, 'etiqette/index.html')
