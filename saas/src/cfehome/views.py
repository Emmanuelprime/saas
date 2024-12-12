from django.http import HttpResponse
from django.shortcuts import render




def home_page_view(request):
    # return HttpResponse("<h1>Home</h1>")
    page_title = "My Page"
    my_context = {
        "page_title":page_title
    }
    return render(request, 'home.html',my_context)