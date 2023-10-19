class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.id = dni
        self.nombre = nombre
        self.apellido = apellido
        self.historico_reservas = {}
    
    def __str__(self) -> str:
        return f"DNI: {self.id}, {self.nombre} {self.apellido}"
    
    def get_id(self) -> str :
        return self.id

    def get_valor(self):
        return self

    def get_nombre(self):
        return self.nombre
    
    def get_reservas_de_cliente(self):
        return self.historico_reservas #Aqui faltan barrabajas

    def add_reserva(self, reserva):
        self.historico_reservas[reserva.get_fecha()] = reserva.get_id_habitacion()
