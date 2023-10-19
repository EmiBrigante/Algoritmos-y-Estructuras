# -*- coding: utf-8 -*-
from Cliente import Cliente
from Habitacion import Habitacion
from Reserva import Reserva
from HashTable import HashTable
class Hotel:
    def __init__(self, num_habitaciones):
        self.hash_cliente=HashTable()
        self.hash_reservas=HashTable()
        self._num_habitaciones = num_habitaciones
        self._habitaciones = []
        self._clientes = []
        self._reservas = []

        # Constantes de error
        self.OK = 1
        self.HABITACION_NO_EXISTE = -1
        self.CLIENTE_NO_EXISTE = -2
        self.RESERVA_NO_EXISTE = -3
        self.HABITACIONES_NO_DISPONIBLES = -4
        self.CLIENTE_NO_TIENE_RESERVAS = -5
        self.FECHA_NO_DISPONIBLE = -6


        for i in range(num_habitaciones):
            self.nueva_habitacion(i)
        
    def __str__(self):
        return f"Hotel con {self._num_habitaciones} habitaciones"

    def nuevo_cliente(self, dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        self.hash_cliente.insertar(cliente.get_id(), cliente)
    
    def __agregar_cliente(self, cliente ):
        self.hash_cliente.insertar(cliente.get_id(), cliente.get_valor())
        self._clientes.append(cliente)

    def nueva_habitacion(self, num_habitacion):
        habitacion = Habitacion(num_habitacion)
        self.__agregar_habitacion(habitacion)
    
    def __agregar_habitacion(self, habitacion ):
        self._habitaciones.append(habitacion)

    def reservar_habitacion(self, num_habitacion, dni_cliente, fecha):
        #Verificar si existe la habitación
        habitacion = self.buscar_habitacion(num_habitacion)
        if habitacion == None:
            self.imprime_errores(self.HABITACION_NO_EXISTE)
            return self.HABITACION_NO_EXISTE 
        

        #Verificar si ya esta resevado para dicha fecha
        if habitacion.esta_reservada(fecha):
            self.imprime_errores(self.FECHA_NO_DISPONIBLE)
            return self.FECHA_NO_DISPONIBLE
        
        #Verificar si existe el cliente
        cliente = self.buscar_cliente(dni_cliente)
        if cliente == None:
            self.imprime_errores(self.CLIENTE_NO_EXISTE)
            return self.CLIENTE_NO_EXISTE
        
        #Crear la reserva y agregarla con el cliente y la habitación
        reserva = Reserva(habitacion, cliente, fecha)
        self._reservas.append(reserva)
        habitacion.add_reserva(reserva)
        cliente.add_reserva(reserva)

        print("Reserva realizada con éxito")
        return self.OK

    def get_reservas_de_cliente(self, dni):
        cliente = self.buscar_cliente(dni)
        if cliente == self.CLIENTE_NO_EXISTE:
            # self.imprime_errores(self.CLIENTE_NO_EXISTE);
            return self.CLIENTE_NO_EXISTE
        
        return cliente.get_reservas_de_cliente()
        
        '''
        for i in range(len(self._reservas)):
            if self._reservas[i].get_id_cliente() == dni:
                reservas_cliente.append(self._reservas[i])
        '''
                
        if len(reservas_cliente == 0 ):
            self.imprime_errores(self.CLIENTE_NO_TIENE_RESERVAS)
        return reservas_cliente

    def buscar_habitacion(self, num_habitacion) -> Habitacion:
        for i in range(len(self._habitaciones)):
            if( self._habitaciones[i].get_id() == num_habitacion ):
                return self._habitaciones[i]
        return None
    
    def buscar_cliente(self, dni) -> Cliente:
        '''
        for i in range(len(self._clientes)):
            if( self._clientes[i].get_id() == dni ):
                return self._clientes[i]
        return None
        '''
        return self.hash_cliente.obtener(dni)

    def buscar_reserva(self, num_reserva):
        for i in range(len(self.hash_reservas)):
            if( self.hash_reservas[i].get_id() == num_reserva ):
                return self.hash_reservas[i]
        return None

    def imprime_errores(self, cod_error):
        errores = {self.HABITACION_NO_EXISTE: "Habitación no existente", 
                   self.CLIENTE_NO_EXISTE: "Cliente no existente", 
                   self.RESERVA_NO_EXISTE: "Reserva no existente", 
                   self.HABITACIONES_NO_DISPONIBLES: "Todas las habitaciones ocupadas",
                   self.OK: "Todo bien", 
                   self.CLIENTE_NO_TIENE_RESERVAS: "El cliente no tiene reservas", 
                   self.FECHA_NO_DISPONIBLE: "Fecha no disponible"
                   }
        print(errores[cod_error])

    def obtener_habitacion_disponible_en_fecha(self, fecha):
        for habitacion in self._habitaciones:
            if not habitacion.esta_reservada(fecha):
                return habitacion
        self.imprime_errores(self.HABITACIONES_NO_DISPONIBLES)
        return None


    def cancelar_reserva(self, id_reserva):
        reserva_to_remove = None
        for reserva in self.hash_reservas:
            if reserva.get_id() == id_reserva:
                reserva_to_remove = reserva
                break
        if reserva_to_remove:
            self.hash_reservas.remove(reserva_to_remove)
            return self.OK
        else:
            self.imprime_errores(self.RESERVA_NO_EXISTE)
            return self.RESERVA_NO_EXISTE

        
    def cancelar_reserva_por_detalle(self, num_habitacion, dni, fecha):
        for i in range(len(self.hash_reservas)):
            if( self.hash_reservas[i].get_fecha() == fecha and self.hash_reservas[i].get_id_cliente == dni and self.hash_reservas[i].get_id_habitacion == num_habitacion):
                self.imprime_errores(self.OK)
        
        return self.RESERVA_NO_EXISTE

    def buscar_hash_reserva(self,num_habitacion,fecha):
        clave = f"{num_habitacion}-{fecha}"
        return self.hash_reservas.obtener(clave)
    
    def insertar_hash_reserva(self,num_habitacion,fecha,cliente):
        clave = f"{num_habitacion}-{fecha}"
        valor = [num_habitacion, fecha, cliente]
        self.hash_reservas.insertar(clave, valor)
        print('Insertado en la tabla hash correctamente')

    def insertar_hash_cliente(self,clave):
        for i in self._clientes:
            if clave == i.get_nombre():
                valor=[i.get_reservas_de_cliente()]
                self.hash_cliente.insertar(clave, valor)
                return
        print('No se ha encontrado al cliente')

    def buscar_hash_cliente(self, nombre):
        clave=nombre
        return self.hash_cliente.obtener(clave)








