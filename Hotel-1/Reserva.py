# -*- coding: utf-8 -*-

class Reserva:
    def __init__(self, habitacion, cliente, fecha):
        self.id = f"{habitacion.get_id()}:{fecha}"
        self.fecha = fecha
        self.id_cliente = cliente.get_id()
        self.id_habitacion = habitacion.get_id()

    def get_id(self):
        return self.id
    
    def get_fecha(self):
        return self.fecha
    def get_valor(self):
        return [self.id_habitacion,self.fecha,self.id_cliente]

    def get_id_cliente(self):
        return self.id_cliente

    def get_id_habitacion(self):
        return self.id_habitacion
    
    def __str__(self) -> str:
        return (f"ID reserva: {self.id}, \nfecha: {self.fecha} "
                f"ID Cliente: {self.id_cliente} \nID Habitación {self.id_habitacion}")