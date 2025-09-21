
#Una forma muy pedestre de hacerlo, podria ser esta
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el primer numero: "))
num3 = float(input("Introduce el primer numero: "))
num4 = float(input("Introduce el primer numero: "))

numeroMayor = max(num1, num2, num3, num4)

print(numeroMayor)


# ---------------------------------------------------------

''' Una aplicación de lista de tareas debería incluir, al menos:
- Insertar y guardar la tarea.
- Vincular esa tarea a un calendario y permitir avisos.
- Borrar o modificar tareas. '''

# ---------------------------------------------------------

''' Interfaz de usuario es todo aquello que permite interactuar con un programa o app:
Botones, ventanas, menús, alertas, mensajes...

Un ejemplo es la pantalla del CRM que uso a diario.'''


# ----------------------------------------------------------

numero = int(input("Introduce un número: "))

for num in range (1,11):
    print(f"{numero} x {num} = {numero * num}")