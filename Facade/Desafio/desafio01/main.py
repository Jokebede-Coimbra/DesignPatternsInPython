
from Facade.Desafio.desafio01.notification_facade import NotificationFacade


notification_facade = NotificationFacade()

notification_facade.send_notification("email", "jkbd@gmail.com", "Corpo do e-mail", "Assunto")
notification_facade.send_notification("sms", "+123456789", "Mensagem SMS")
notification_facade.send_notification("push","123456", "Mensagem Push")
