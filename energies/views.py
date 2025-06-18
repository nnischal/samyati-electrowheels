from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.timezone import now
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
            instance = form.save()
            
            # Email to Administrator
            subject_admin = f"New Contact Form Submission from {instance.name}"
            message_admin =f"""
You have received a new message from the contact form.
Name: {instance.name}
Email: {instance.email}
Contact:{instance.contact}
Message: 
{instance.message}
"""
            send_mail(
                subject_admin,
                message_admin,
                settings.DEFAULT_FROM_EMAIL,  
                [settings.CONTACT_EMAIL],  
                fail_silently=False,
            )
            # 2. Thank-you email to the User(With HTML/CSS content)
            subject_user = "Thank you for contacting Samyati Energies"
            context = {
                'name': instance.name,
                'message': instance.message,
                'now': now(),
            } 
            html_content = render_to_string('emails/thank_you.html', context)
            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(
                subject=subject_user,
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[instance.email]
            )
            email.attach_alternative(html_content, "text/html")
            email.send()

            messages.success(request, "Your message has been sent successfully! Thank you for reaching out.")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'energies/contact.html', {'form': form})