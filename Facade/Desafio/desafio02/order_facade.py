from notification_system import NotificationSystem
from payment_system import PaymentSystem
from order_system import OrderSystem


class OrderFacade:
    
    def __init__(self) -> None:
       self.order_system = OrderSystem()
       self.payment_system =  PaymentSystem()
       self.notification_system = NotificationSystem()
       
    def place_order(self, items):
        self.order_system.place_order(items)
        return (f"Pedido criado: {', '.join(items)}")
    
    def process_payment(self, amount):
        self.payment_system.process_payment(amount)
        return (f"Pagamento processado no valor de ${amount}")
    
    def notify_customer(self, message):
        self.notification_system.notify_customer(message)
        return (f"Notificação enviada ao cliente: {message}")
        