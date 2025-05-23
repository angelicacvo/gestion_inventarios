# Inicialización de variables y diccionario vacío
product_name = ""
price = ""
quantity = ""
inventory = {}

# Inicialización de variables y diccionario vacío
def validate_str(value):
  return value.strip() != "" and value.isalpha()

# Inicialización de variables y diccionario vacío
def validate_num(value):
  return value.isdigit() and int(value) > 0

# Función que recibe los parametros product_name, price y quantity y crea el diccionario de productos con sus respectivos valores.
def create_product(product_name, price, quantity):
  flag = "s"
  while flag != "n":
    product_name = input("Ingresa el nombre del producto ")
    if not validate_str(product_name):
      print("Error. Ingresa un valor válido")
    if product_name in inventory:
      print("Este artículo ya se encuentra en el inventario, si deseas puedes actualizarlo")
      return

    price = input("Ingresa el precio del producto ")
    quantity = input("Ingresa la cantidad del producto ")
    if not validate_num(price) and validate_num(quantity):
      print("Error. Ingresa un valor válido")
      continue
    inventory[product_name] = {"Precio": price, "Cantidad": quantity}
    print(f"El producto {product_name} fue añadido exitosamente")
    # el usuario debe presionar n o no para salir del programa.
    choice = input("¿deseas ingresar otro producto? [s/n]").lower()
    match choice:
      case "n":
        break

# Función que verifica que el nombre del producto exista en el diccionario e imprime los valores si los encuentra. Retorna dos valores (price y quantity) o None.
def get_product():
    product_name = input("Ingresa el nombre del producto ")
    if not validate_str(product_name):
      print("Error. Ingresa un valor válido")
      return
    if product_name in inventory:
      price = inventory[product_name]['Cantidad']
      quantity = inventory[product_name]['Precio']
      print("Nombre: ", product_name)
      print("Cantidad: ", price)
      print("Precio: ", quantity)
      return price, quantity
    else:
       print("El producto no existe en el inventario")

# Función que verifica que el nombre del producto exista en el diccionario e imprime los valores si los encuentra. Retorna dos valores (price y quantity) o None.
def update_product():
  product_name = input("Ingresa el nombre del producto ")
  if product_name in inventory:
    while True:
      update_product = input("Ingrese un nuevo precio: ")
      if not validate_num(update_product):
        print("Error. Ingresa un valor válido")
        continue
      inventory[product_name]['Precio'] = int(update_product)
      print(f"Su producto: {product_name} fue actualizado con éxito. Su nuevo precio es: {update_product}")
      break
  else:
    print("Producto no existente")

# Función que verifica que el nombre del producto exista en el diccionario e imprime los valores si los encuentra. Retorna dos valores (price y quantity) o None.
def delete_product():
  product_name = input("Ingresa el nombre del producto ")
  if product_name in inventory:
    inventory.pop(product_name)
    print(inventory)
  else:
    print("Producto no encontrado")
    

# Función que verifica que el nombre del producto exista en el diccionario e imprime los valores si los encuentra. Retorna dos valores (price y quantity) o None.
def calculate_inventory():
  total = 0
  multiplication = lambda x, y: x * y
  for product_name in inventory:
    multiplication_for_product = multiplication(int(inventory[product_name]['Precio']), int(inventory[product_name]['Cantidad']))
    total = total + multiplication_for_product
  print(f"El total del inventario actual es: {total}")

# utilización de las funciones dentro de cada opción del menú
def menu():
  option = input("""
  Bienvenido a tu inventario. Ingresa la opción que deseas realizar
  \n[1] Agregar producto al inventario
  \n[2] Consultar producto del inventario
  \n[3] Actualizar precio del inventario
  \n[4] Eliminar producto del inventario
  \n[5] Calcular el valor total del inventario
  \n[6] Salir del sistema de inventarios

  """)
  return option

flag = True
while flag != 6:
  match menu():
    case "1": create_product(product_name, price, quantity)
    case "2": get_product()
    case "3": update_product()
    case "4": delete_product()
    case "5": calculate_inventory()
    case "6":
      break
    # Si la persona ingresa un valor diferente va a generar un error.
    case _:
      print("Opción no válida")
