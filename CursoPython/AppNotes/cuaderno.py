import datetime

ultima_id = 0


class Nota:
    """Representa una nota en el cuaderno. Se compara con un String en las busquedas y las etiquetas para cada nota"""

    def __init__(self, memo, tags=""):
        """inicializa una nota con memo y tags opcionales
        separados por comas. Automáticamente se confiura la fecha de creación e id unico"""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()

        global ultima_id
        ultima_id += 1
        self.id = ultima_id

    def match(self, filter) -> True:
        """Determina si esta nota concuerda con el filtro de text.
        Devuelve true si concuerda o False.
        La busqueda es case sensitive y compara tanto en el contenido como en las tags"""

        return filter in self.memo or filter in self.tags


class Cuaderno:
    """representa una colección de notas"""

    def __init__(self):
        """Inicia un cuaderno con una lista vacía"""
        self.notas = []

    def _encontrar_nota(self, nota_id):
        """Devuelve la nota con la correspondiente id"""
        for nota in self.notas:
            if nota.id == nota_id:
                return nota

    def nueva_nota(self, memo, tags=""):
        """Crea una nueva nota y la añade a la lista"""
        self.notas.append(Nota(memo, tags))

    def modificar_memo(self, nota_id, memo):
        """Encuentra la nota de la id correspondiente y cambia su contenido al  valor dado"""
        self._encontrar_nota(nota_id).memo = memo

    def modificar_tags(self, nota_id, tags):
        """Encuentra la nota por el id pero lo que cambia son los tags"""
        self._encontrar_nota(nota_id).tags = tags

    def search(self, filter):
        """Enceuntra todas las notas que coincidan con el filtro string dado"""
        return [nota for nota in self.notas if nota.match(filter)]
