from django.http import HttpResponse
from django.shortcuts import render
from.models import place,special
# Create your views here.
def fun(request):
    obj=place.objects.all()
    abc = special.objects.all ()
    return render(request,"index.html",{'results':obj,'late':abc})



# def latest(request):
#     abc=special.objects.all()
#     return render(request,"index.html",{'late':abc})