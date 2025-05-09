product_name = ""
price = ""
quantity = ""
inventory = {}

def validate_str(value):
  return value.strip() != "" and value.isalpha() 

def validate_num(value):
  return value.isdigit() and int(value) > 0

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
    if not validate_num(price) or validate_num(quantity):
      print("Error. Ingresa un valor válido")
      continue
    inventory[product_name] = {"Precio": price, "Cantidad": quantity}
    print(f"El producto {product_name} fue añadido exitosamente")    
    choice = input("¿deseas ingresar otro producto? [s/n]").lower()
    match choice:
      case "n":
        break

def get_product():
    product_name = input("Ingresa el nombre del producto ")
    if not validate_str(product_name):
      print("Error. Ingresa un valor válido")
      return None, None
    if product_name in inventory:
      price = inventory[product_name]['Precio']
      quantity = inventory[product_name]['Cantidad']
      print("Nombre: ", product_name)
      print("Cantidad: ", price)
      print("Precio: ", quantity)
      return price, quantity
    else:
      print("El producto no existe en el inventario")    
      return None, None

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

def delete_product():
  product_name = input("Ingresa el nombre del producto ")
  if product_name in inventory:
    inventory.pop(product_name)
    print(f"Tu producto: {product_name} fue eliminado con éxito")
  else:
    print("Producto no encontrado")
    
def calculate_inventory():
  total = 0
  multiplication = lambda x, y: x * y
  for product_name in inventory:
    multiplication_for_product = multiplication(inventory[product_name]['Precio'], inventory[product_name]['Cantidad'])
    total = total + multiplication_for_product
  print(f"El total del inventario actual es: {total}")

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
    case _:
      print("Opción no válida")
