class ArchivoAudio:
    """"""

    def __init__(self, nombrearchivo):
        if not nombrearchivo.endswith(self.ext):
            print("formato archivo no valido")
        self.nombrearchivo = nombrearchivo


class ArchivoMP3(ArchivoAudio):
    """"""

    ext = "mp3"

    def play(self):
        print(f"ejecutando {self.nombrearchivo} como mp3")


class ArchivoWAV(ArchivoAudio):
    """"""

    ext = "wav"

    def play(self):
        print(f"ejecutando {self.nombrearchivo} como wav")


class ArchivoOGG(ArchivoAudio):
    """"""

    ext = "ogg"

    def play(self):
        print(f"ejecutando {self.nombrearchivo} como ogg")


def main():
    mp3 = ArchivoMP3("archivo.mp3")
    ogg = ArchivoOGG("archivo.ogg")
    wav = ArchivoWAV("archivo.wav")

    mal = ArchivoMP3("archivo.wav")

    mp3.play()
    ogg.play()
    wav.play()

    mal.play()


if __name__ == "__main__":
    main()
