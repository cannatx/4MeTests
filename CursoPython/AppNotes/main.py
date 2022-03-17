import menu
from cuaderno import Cuaderno, Nota


def main():
    """"""
    c = Cuaderno()
    c.nueva_nota("Esta es mi primera nota del cuaderno")
    c.nueva_nota("Esta es otra entrada")

    # imprimimos los ids de las notas presentes
    for nota in c.notas:
        print(nota.id)

    # accedemos a los strings de las notas
    for nota in c.notas:
        print(nota.memo)

    # vemos el contenido de la nota 2 y lo modificamos
    print(f"el contenido de la nota dos es: {c.notas[1].memo}")
    c.modificar_memo(2, "Contenido de la segunda nota modificado")
    print(f"Ahora el contenido de la nota dos es: {c.notas[1].memo}")

    m = menu.Menu()
    m.run()


if __name__ == "__main__":
    main()
