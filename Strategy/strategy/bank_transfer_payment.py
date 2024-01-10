from interface.payment_strategy import PaymentStrategy

class BankTransferPayment(PaymentStrategy):
    def process_payment(self, amount):
       print(f"Payment of ${amount} processed via Bank Transfer")