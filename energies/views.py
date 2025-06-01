from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
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
            # Send email using Django's send_mail function
            instance = form.save()
            subject = f"New Contact Form Submission from {instance.name}"
            message =f"""
You have received a new message from the contact form.
Name: {instance.name}
Email: {instance.email}
Contact:{instance.contact}
Message: {instance.message}"""
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,  
                [settings.CONTACT_EMAIL],  
                fail_silently=False,
            )
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  # You can redirect to a success page
    else:
        form = ContactForm()
    
    return render(request, 'energies/contact.html', {'form': form})
