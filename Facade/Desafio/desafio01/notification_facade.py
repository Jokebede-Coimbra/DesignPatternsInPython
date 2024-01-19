from Facade.Desafio.desafio01.email_service import EmailService
from Facade.Desafio.desafio01.push_notification_service import PushNotificationService
from Facade.Desafio.desafio01.sms_service import SMSService


class NotificationFacade:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SMSService()
        self.push_notification_service = PushNotificationService()

    def send_notification(self, type, recipient, message, subject= None):
        if type == "email":
            self.email_service.send_email(recipient, subject, message)
        elif type == "sms":
            self.sms_service.send_sms(recipient, message)
        elif type == "push":
            self.push_notification_service.send_push_notification(recipient, message)
        else:
            print("Tipo de notificação não suportado.")
