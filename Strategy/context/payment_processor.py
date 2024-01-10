class PaymentProcessor:
    
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy
    
    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy
        
    def process_payment(self, amount):
        self.payment_strategy.process_payment(amount)  