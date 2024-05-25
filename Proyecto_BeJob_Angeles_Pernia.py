# Importamos la librería para manejar excepciones
import sys

# Definimos la clase Tarea con dos atributos: descripción y completada
class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

# Definimos la clase ListaTareas con un atributo: tareas (una lista vacía)
class ListaTareas:
    def __init__(self):
        self.tareas = []

    # Método para agregar una nueva tarea a la lista
    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)

    # Método para marcar una tarea como completada según su posición
    def marcar_completada(self, posicion):
        if 0 <= posicion < len(self.tareas):
            self.tareas[posicion].completada = True
        else:
            raise IndexError("La posición especificada no es válida.")

    # Método para mostrar todas las tareas pendientes
    def mostrar_tareas(self):
        for i, tarea in enumerate(self.tareas):
            estado = "[x]" if tarea.completada else "[ ]"
            print(f"{i+1:02}. {estado} {tarea.descripcion}")

    # Método para eliminar una tarea según su posición
    def eliminar_tarea(self, posicion):
        if 0 <= posicion < len(self.tareas):
            del self.tareas[posicion]
        else:
            raise IndexError("La posición especificada no es válida.")

# Definimos la clase Aplicacion con un atributo: lista\_tareas (una instancia de ListaTareas)
class Aplicacion:
    def __init__(self):
        self.lista_tareas = ListaTareas()

    # Método para manejar el menú de opciones del usuario
    def manejar_menu(self):
        while True:
            print("\nTareas pendientes:")
            self.lista_tareas.mostrar_tareas()
            print("\n¿Qué desea hacer?")
            print("1. Agregar tarea")
            print("2. Marcar tarea como completada")
            print("3. Eliminar tarea")
            print("4. Salir")

            try:
                opcion = int(input("Ingrese el número de la opción deseada: "))
            except ValueError:
                print("Error: La opción debe ser un número.")
                continue

            if opcion == 1:
                descripcion = input("Ingrese la descripción de la tarea: ")
                self.lista_tareas.agregar_tarea(descripcion)
            elif opcion == 2:
                try:
                    posicion = int(input("Ingrese la posición de la tarea a marcar como completada: "))
                    self.lista_tareas.marcar_completada(posicion - 1) # Restamos 1 porque las posiciones comienzan en 0
                except IndexError as e:
                    print(e)
            elif opcion == 3:
                try:
                    posicion = int(input("Ingrese la posición de la tarea a eliminar: "))
                    self.lista_tareas.eliminar_tarea(posicion - 1) # Restamos 1 porque las posiciones comienzan en 0
                except IndexError as e:
                    print(e)
            elif opcion == 4:
                print("Hasta luego!")
                sys.exit(0)
            else:
                print("Error: La opción debe ser un número entre 1 y 4.")

# Instanciamos la clase Aplicacion y llamamos al método manejar_menu
if __name__ == "__main__":
    aplicacion = Aplicacion()
    aplicacion.manejar_menu()