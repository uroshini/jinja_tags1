from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':10000,'b':100,'c':1000}
    return render(request,'conditions.html',d)