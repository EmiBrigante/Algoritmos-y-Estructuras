class Habitacion:
    def __init__(self, num_habitacion):
        self.num_habitacion = num_habitacion
        self.historico_reservas = {} # fecha: reserva

    def get_id(self):
        return self.num_habitacion 
    
    def esta_reservada(self, fecha) -> bool:
        return fecha in self.historico_reservas
    
    def add_reserva(self, reserva):
        self.historico_reservas[reserva.get_fecha()] = reserva
    
    def get_historico_reservas(self):
        return self.historico_reservas
    
    def __str__(self) -> str:
        return f"Num. habitación: {self.num_habitacion}"