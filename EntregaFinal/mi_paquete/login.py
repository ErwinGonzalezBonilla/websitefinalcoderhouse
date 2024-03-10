Base_de_datos={}
def registrar_usuario():
  Nombre=input("Nobre de usuario: ")
  Clave=input("Crea una clave: ")
  if Nombre not in Base_de_datos:
   Base_de_datos[Nombre] = Clave
   print("SU REGISTRO HA SIDO EXITOSO")
def iniciar_sesion():
  Nombre=input("Coloque su Nombre de Usuario: ")
  Clave=input("Coloque su clave secreta: ")
  if Nombre in Base_de_datos and Base_de_datos[Nombre] == Clave:
    print("!BIENVENIDO¡ usted forma parte de nuestra base de datos.")
  else:
    print("HA OCURRIDO UN ERROR, su Nombre de Usuario o Clave son incorrectas.")
while True:
  print(">>>")
  print("r- Registrar Usuario")
  print("i- Iniciar Sesión")
  print("s- Salir")
  opcion =input("Seleccione: (r) para registrarse, (i) para ingresar o (s) para salir ")
  if opcion == "r":
    registrar_usuario()
  elif opcion == "i":
    iniciar_sesion()
  elif opcion == "s":
    print("¡GRACIAS, vuelva pronto!")
    break
  else:
        print("OPCIÓN NO VÁLIDA. Por favor seleccione una opción: (r), (i) o (s).")
        