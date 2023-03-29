from django.shortcuts import render
from .models import Acronym

# Create your views here.
def index(request):
    """The home page view for acronym app."""
    acronym_details = ""
    if request.method == "POST":
        try:
            acronym_details = Acronym.objects.get(acronym=request.POST.get('acronym').upper()) 
        except:
            acronym_details = "nf"
    
    content = {
        'acronym_details' : acronym_details
    }
    return render(request,'core/index.html',content)