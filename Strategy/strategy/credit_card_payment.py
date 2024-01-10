from interface.payment_strategy import PaymentStrategy

class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Payment of ${amount} processed via Credit Card")
