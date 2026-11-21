from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def landing_view(request) :
    # context = {
    #     'name' : 'Ajay',
    #     'branch' : 'History',
    #     'marks' : [10, 20, 30],
    #     'address' : {
    #         'at' : 'abc',
    #         'po' : 'xyz',
    #         'pin' : 112233,
    #         'state' : 'Odisha'
    #     }
    # }
    # return render(request, 'landing.html', data)
def landing_view(request) :
    ''' 
    context is the data which is passed from the views
    to the template in dictionary format.

    the keys of the dict will be used as variable names in template and 
    the values assigned to the keys will be retrived as values of those 
    variables.
    '''
    return render(request, 'landing.html', context={
        'name' : 'Ajay',
        'branch' : 'History',
        'marks' : [10, 20, 30],
        'address' : {
            'at' : 'abc',
            'po' : 'xyz',
            'pin' : 112233,
            'state' : 'Odisha'
        }
    })

def username(request, username) :
    # return HttpResponse(f'<h1>User name : {username} <h1>')
    return render(request, 'username.html', context= {
        'username' : username
    })
def add(request, first, second) :    
    return HttpResponse(f'<h1>the sum is : {first+second} </h1>')

def check_prime_view(request, number) :
    is_prime = True
    for i in range(2, number) :
        if number % i == 0 :
            is_prime = False
            break
    if is_prime :
        return HttpResponse('<h1>Prime Number</h1>')
    else :  
        return HttpResponse('<h1>Not Prime Number</h1>')