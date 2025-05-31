from django.shortcuts import render, redirect
from .forms import ContactForm

def home(request):
    return render(request, 'energies/home.html')

def products(request):
    return render(request, 'energies/products.html')

def why_lithium(request):
    return render(request, 'energies/why_lithium.html')
def about(request):
    return render(request, 'energies/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # You can redirect to a success page
    else:
        form = ContactForm()
    
    return render(request, 'energies/contact.html', {'form': form})
