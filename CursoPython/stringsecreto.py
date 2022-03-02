class StringSecreto:
    """Un modo no totalmente seguro de almacenar un string"""

    def __init__(self, string_plano, frase_pass):
        self.__string_plano = string_plano
        self.__frase_pass = frase_pass

    def decrypt(self, frase_pass):
        if frase_pass == self.__frase_pass:
            return self.__string_plano
        else:
            return ""


def main():
    string_secreto = StringSecreto("esta es la frase a ocultar", "contraseña")
    print(string_secreto.decrypt("shome"))
    print(string_secreto.decrypt("contraseña"))
    # Las varaibles que se asignan con el doble subrayado "name mangling" hace que haya que acceder
    # al dato con un guin delante de la clase (_NombreClase)
    print(string_secreto._StringSecreto__string_plano)


if __name__ == "__main__":
    main()
