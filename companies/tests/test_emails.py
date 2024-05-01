from django.core import mail
from django.test import TestCase
from django.conf import settings
from django.test import Client
import json
from unittest.mock import patch  # Import patch from unittest.mock

class EmailUnitTest(TestCase):
    def test_send_email_should_succeed(self) -> None:
        with self.settings(
            EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
 
        ):
            self.assertEqual(len(mail.outbox),0)
            # Example usage of send_mail
            mail.send_mail(
                'Test Subject here',
                'Here is the message.',
                settings.DEFAULT_EMAIL_FROM,
                ['yogesh.baraskar@softude.com'],
                fail_silently=False,
            )
            
            self.assertEqual(len(mail.outbox),1)
            self.assertEqual(mail.outbox[0].subject,'Test Subject here')

    # def test_send_email_without_arguments_should_send_empty_email(self) -> None:
    #     client =Client()
    #     with patch(
    #         'companies.views.send_mail'
    #         ) as mocked_send_mail_function:
    #             response = client.post(path="/send-email")
    #             response_content =  json.loads(response.content)
    #             self.assertEqual(response.status_code,400)
    #             self.assertEqual(response_content["status"],"success")
    #             self.assertEqual(response_content["info"],"email sent successfully")
    #             mocked_send_mail_function.assert_called_with(
    #                 subject = None,
    #                 message = None,
    #                 email_from = settings.DEFAULT_EMAIL_FROM,
    #                 reciepient_list = ['yogesh.baraskar@softude.com'],
    #                 fail_silently=False,
    #             )
