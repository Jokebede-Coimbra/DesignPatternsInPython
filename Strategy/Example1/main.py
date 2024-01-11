from strategy.bank_transfer_payment import BankTransferPayment
from strategy.credit_card_payment import CreditCardPayment
from strategy.pay_pal_payment import PayPalPayment
from context.payment_processor import PaymentProcessor


amount_to_pay = 100.0

# Criando estratégias de pagamento
credit_card_strategy = CreditCardPayment()
paypal_strategy = PayPalPayment()
bank_transfer_strategy = BankTransferPayment()

# Criando o contexto com a estratégia inicial (Cartão de Crédito)
payment_processor = PaymentProcessor(credit_card_strategy)
payment_processor.process_payment(amount_to_pay)

# Mudando dinamicamente para PayPal
payment_processor.set_payment_strategy(paypal_strategy)
payment_processor.process_payment(amount_to_pay)

# Mudando dinamicamente para Transferência Bancária
payment_processor.set_payment_strategy(bank_transfer_strategy)
payment_processor.process_payment(amount_to_pay)
