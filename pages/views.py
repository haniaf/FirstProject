from django.shortcuts import render

from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        'my_text' : 'from About context, text',
        'my_number' : 'from About context, number',
        'my_list' : ['a', 'b', 'c'],
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})