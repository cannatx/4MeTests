import sys

from cuaderno import Cuaderno, Nota


class Menu:
    """Muestra un menu y responde a las elecciones"""

    def __init__(self):
        self.cuaderno = Cuaderno()

        self.elecciones = {
            "1": self.mostrar_notas,
            "2": self.search_notas,
            "3": self.add_nota,
            "4": self.modificar_nota,
            "5": self.quit,
        }

    def mostrar_menu(self):
        print(
            """
        Menu Cuaderno
        
        1 Mostrar todas las Notas
        2 Buscar Notas
        3 Añadir Nota
        4 Modificar Nota
        5 Salir
        """
        )

    def run(self):
        """Muestra el menu y responde a la elección"""
        while True:
            self.mostrar_menu()
            eleccion = input("Escribe una opcion: ")
            accion = self.elecciones.get(eleccion)
            if accion:
                accion()
            else:
                print(f"{eleccion} no es una opcion valida.")

    def mostrar_notas(self, notas=None):
        if not notas:
            notas = self.cuaderno.notas
        for nota in notas:
            print(f"{nota.id}: nota.tags", nota.memo)

    def search_notas(self):
        filter = input("Buscar por: ")
        notas = self.cuaderno.search(filter)
        self.mostrar_notas(notas)

    def add_nota(self):
        memo = input("Escribe un memo: ")
        self.cuaderno.nueva_nota(memo)
        print("Nota añadida.")

    def modificar_nota(self):
        id = input("Escribe el id de la nota: ")
        memo = input("Escribe un memo: ")
        tags = input("Escribe tags: ")
        if memo:
            self.cuaderno.modificar_memo(id, memo)
        if tags:
            self.cuaderno.modificar_tags(id, tags)

    def quit(self):
        print("Gracias por usar tu cuadernohoy...")
        sys.exit(0)
