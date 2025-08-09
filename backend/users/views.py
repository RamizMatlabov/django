from django.shortcuts import render
from .models import Profile

def home(request):
    context = {
        "my_name": "Ramiz",
        "profile": Profile.objects.first()
    }
    return render(request, 'index.html', context)
