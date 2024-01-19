class PushNotificationService:
    
    def send_push_notification(self, device_id, message):
        print(f"Enviando notificação push para dispositivo {device_id}: '{message}'")