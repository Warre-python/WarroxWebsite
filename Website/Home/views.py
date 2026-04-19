from django.shortcuts import render

# Create your views here.


def home(request):
    # Django vindt dit nu in frontend/templates/frontend/index.html
    return render(request, 'frontend/index.html')

def terminal(request):
    return render(request, 'frontend/terminal.html')