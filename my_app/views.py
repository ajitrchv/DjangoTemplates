from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def example_view(request):
    return render(request, 'my_app/example.html')

def variable_view(request):
    
    my_var = {
        'fname':'Hard','lname':'pope',
        'some_list':[1,2,3],'some_dict':{'inside_key':'inside_value'}
    }
    
    return render(request,'my_app/variable.html', context =my_var)