from django.shortcuts import redirect
from .models import Contact

def submit_contact(request):
    if request.method == "POST":
        Contact.objects.create(
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            city=request.POST.get('city'),
        )
        return redirect('/')   # back to landing page
