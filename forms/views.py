from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .models import Contact

@csrf_exempt
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        if not all([name, email, phone, message]):
            return JsonResponse({'success': False, 'error': 'All fields are required.'}, status=400)

        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()

        # Prepare email
        subject = 'New Contact Form Submission'
        text_content = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
        html_content = f'''
        <html>
        <body>
            <div style="padding:50px; border:2px solid gray; border-radius:20px;">
                <img src="https://pythoncoding2263.pythonanywhere.com/static/img/logo.png" width:80px;> 
                <h2>New Contact Form Submission</h2>
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Phone:</strong> {phone}</p>
                <p><strong>Message:</strong> {message}</p>
            </div>
        </body>
        </html>
        '''
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.CONTACT_EMAIL]

        try:
            email = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
            email.attach_alternative(html_content, "text/html")
            email.send()
            contact.email_sent = True
            contact.save()
            return JsonResponse({'success': True, 'message': 'Thank you for your message!'}, status=201)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    return JsonResponse({'success': False, 'error': 'Invalid request method.'}, status=405)
