from Hotel import Hotel

prueba_2=Hotel(100)

prueba_2.nuevo_cliente("123456", "John", "Doe")

#print(prueba_2.get_reservas_de_cliente("123456"))

#print(prueba_2.buscar_hash_cliente("123456"))

prueba_2.nuevo_cliente("123457", "Juan", "Gallego")
prueba_2.buscar_hash_cliente("123457")

#print(prueba_2.buscar_hash_cliente("123457"))

prueba_2.nueva_habitacion("89")
print(prueba_2.buscar_habitacion("89"))
prueba_2.reservar_habitacion("89", "123457", "02-05-2023")


