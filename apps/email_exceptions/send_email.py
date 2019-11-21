
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

class NotificarException:

    def enviar_mensaje(self, invocacion, contenido):
        subject = 'Excepcion a las %s en %s' % (timezone.now(), invocacion)
        message = '%s' % (contenido)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['cdanielhdezperez@gmail.com',]
        send_mail( subject, message, email_from, recipient_list )