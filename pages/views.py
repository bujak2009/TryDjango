from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {'contact_mail': 'My e-mail adress is !@#$%', 'age': 'Only for 18+'})

def about_view(request, *args, **kwargs):
    my_context = {
        'my_text': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
        'my_number': 123,
        'my_list': [123, 455657, 'abc', 3.14, 'Anzej']
    }
    return render(request, 'about.html', my_context)

def social_view(request, *args, **kwargs):
    return HttpResponse('<h1>Social Page</h1')


# Create your views here.
