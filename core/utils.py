from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse
from .tokens import my_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.conf import settings
import jwt
import datetime
from django.http import HttpResponse


def send_html_email_with_file(subject, to, html_file_path, context=None) -> bool:
    try: 

        html_content = render_to_string(html_file_path, context) # render with dynamic value
        text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.

        # create the email, and attach the HTML version as well.
        msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return True

    except Exception as e:
        print(e)
        return False

def encode_token(user, prefix_url):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    token = jwt.encode({'user': user, 'exp': expiration_time}, settings.SECRET_KEY, algorithm='HS256')
    
    new_link = reverse(f'core:{prefix_url}', args=[token])
    return settings.PRIMARY_URL + new_link

def decode_token(token):

    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        # rest of your code...
        print(decoded_token)
    except jwt.ExpiredSignatureError:
        return HttpResponse("Token has expired")
    except jwt.InvalidTokenError:
        return HttpResponse("Invalid token")

def create_link_with_token(user, prefix_url):
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = my_token_generator.make_token(user)
    reset_password_link = reverse(f'core:{prefix_url}', args=[uidb64, token])

    return settings.PRIMARY_URL + reset_password_link       

def is_token_valid(token, user, expiration_duration_in_seconds):
    try:
        # Decode the token to extract user and timestamp information
        checked_result = my_token_generator.check_token(user, token)
       
        return checked_result
    except Exception as e:
        # Token is invalid or expired
        return False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          