from django.shortcuts import render

# Create your views here.
def bulls_n_cows(request):
    return render(request, 'index.html')

