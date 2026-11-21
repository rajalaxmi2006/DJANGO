from django.shortcuts import render

# Create your views here.
def biodata_view(request) :
    return render(request,'biodata.html') 