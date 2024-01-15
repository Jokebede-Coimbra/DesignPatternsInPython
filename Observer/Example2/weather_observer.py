# Observer (Observador)
class WeatherObserver:
    def update(self, temperature):
        raise NotImplementedError("Método 'update' deve ser implementado nas subclasses.")
