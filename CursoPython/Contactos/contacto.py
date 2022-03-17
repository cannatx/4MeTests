# Ejemplo de herencias

# Ejemplo de herencia de una superclase llamada list
# Para extender funciones predeterminadas
class ListaContactos(list):
    def buscar(self, nombre):
        """Devuelve todos los contactos que coincidan con la busqueda"""

        return [contacto for contacto in self if nombre in contacto.nombre]


# Superclase
class Contacto:
    # todos_contactos = list()
    todos_contactos = ListaContactos()

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        Contacto.todos_contactos.append(self)


class EnviarEmal:
    def enviar_email(self, mensaje):
        """Ejemplo vacio de funcion para enviar emails"""
        print("enviando mensaje a {self.email}")


#  y ejemplo de Herencia multiple
class EnvioEmailContactos(Contacto, EnviarEmal):
    pass


class ContenedorDireccion:
    def __init__(self, calle, ciudad, provincia, cp):
        self.calle = calle
        self.ciudad = ciudad
        self.provincia = provincia
        self.codigo = cp


# Subclase que hereda de contacto
# también se puede sobreescribir un método
# Con la metodo Super se pueden llamar los atributos de la clase padre cuando se sobreescribe
class Vendedor(Contacto):
    def __init__(self, nombre, email, telefono):
        super().__init__(nombre, email)
        self.telefono = telefono

    def pedido(self, pedido):
        print("En una aplicacion completa enviaría un pedido")


# extender alguna funcion de un diccionario en una subclase
class NombreLargoDict(dict):
    """Simplemente devuelve la key con mas caracteres del diccionario"""

    def clave_maslarga(self):
        maslarga = None
        for key in self:
            if not maslarga or len(key) > len(maslarga):
                maslarga = key
        return maslarga


def main():
    c = Contacto("Scarlett Johansson", "scarlet@suenail.com")
    v = Vendedor("Bic Inc.", "bic@empresa.com", "2342524525")

    c2 = Contacto("Juan A", "juana@suemail.com")

    print(c.todos_contactos.buscar("Juan")[0].email)
    #
    clavelarga = NombreLargoDict()
    clavelarga["hola"] = 1
    clavelarga["Un poco"] = 1
    clavelarga["mas larga"] = 1
    clavelarga["o bastante mas larga"] = 1

    print(clavelarga.clave_maslarga())

    pass


if __name__ == "__main__":
    main()
