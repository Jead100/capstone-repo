from django.shortcuts import render
from datetime import datetime

def index(request):
    current_year = datetime.now().year
    return render(request, 'index.html', {'current_year': current_year})

