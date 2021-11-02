from django.shortcuts import render

# Create your views here.
def home_page_view(request, *args, **kwargs):
    return render(request, 'base.html', {})

def sign_in_view(request, *args, **kwargs):
    return render(request, 'signin.html', {})

