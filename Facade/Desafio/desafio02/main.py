
from order_facade import OrderFacade


order_facade = OrderFacade()

order_result = order_facade.place_order(["Tapioca", "Sorvete", "Suco"]);
print(order_result)

payment_result = order_facade.process_payment(40.0);
nottification_result = order_facade.notify_customer("Seu pedido está a caminho!")

print(payment_result)
print(nottification_result)