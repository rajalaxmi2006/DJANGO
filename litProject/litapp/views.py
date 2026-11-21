from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'index.html' , name='home')

def exam_view(request):
    return render(request, 'exam.html', name='exam')