from django.http import HttpResponse
from django.shortcuts import render
from visits.models import Visit




def home_page_view(request):
    # return HttpResponse("<h1>Home</h1>")
    qs = Visit.objects.all()
    page_qs = Visit.objects.filter(path=request.path)
    try:
        percent = (page_qs.count() * 100) / qs.count()
    except:
        percent = 0
    page_title = "My Page"
    my_context = {
        "page_title":page_title,
        "page_visit_count": page_qs.count(),
        "percent":percent
        
    }
    Visit.objects.create(path=request.path)
    return render(request, 'home.html',my_context)