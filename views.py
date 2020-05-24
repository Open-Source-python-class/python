from django.shortcuts import render

# Create your views here.
def male(request):
    return render(request, 'male.html')


def female(request):
    return render(request, 'female.html')