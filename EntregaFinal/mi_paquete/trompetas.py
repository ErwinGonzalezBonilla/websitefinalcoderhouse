class Cliente:
    def __init__(self, nombre, apellido, email, forma_pago):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.forma_pago = forma_pago

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nEmail: {self.email}\nForma de Pago: {self.forma_pago}"


class Trompeta:
    def __init__(self, modelo):
        self.modelo = modelo

    def __str__(self):
        return f"Modelo de Trompeta: {self.modelo}"

nombre_cliente = input("Ingrese su nombre: ")
apellido_cliente = input("Ingrese su apellido: ")
email_cliente = input("Ingrese su email: ")
forma_pago_cliente = input("Ingrese su forma de pago: ")

cliente = Cliente(nombre_cliente, apellido_cliente, email_cliente, forma_pago_cliente)

print("\n¡Bienvenido a la tienda de trompetas!\n")
print(cliente)

modelos_trompetas = ["Trompeta Sib", "Trompeta en Do", "Trompeta Piccolo", "Flugelhorn", "Corneta Sib"]

print("\nModelos de Trompetas Disponibles:")
for idx, modelo in enumerate(modelos_trompetas, start=1):
    print(f"{idx}. {modelo}")

opcion_trompeta = int(input("\nSeleccione el número del modelo de trompeta que desea comprar: "))
modelo_elegido = modelos_trompetas[opcion_trompeta - 1]

trompeta_cliente = Trompeta(modelo_elegido)
print("\n¡Excelente elección!\n")
print(trompeta_cliente)


