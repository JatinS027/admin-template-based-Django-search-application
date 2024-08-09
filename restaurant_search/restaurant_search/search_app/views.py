from django.shortcuts import render
from .models import Restaurant

def search(request):
    query = request.GET.get('q')
    results = Restaurant.objects.filter(dish__icontains=query) if query else []
    return render(request, 'search_app/search.html', {'results': results, 'query': query})
