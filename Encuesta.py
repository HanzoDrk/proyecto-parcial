class Pregunta:
    def _init_(self, texto):
        self.texto = texto
        self.respuestas = []

    def registrar_respuesta(self, respuesta):
        self.respuestas.append(respuesta)

    def mostrar_resultado(self):
        print(f"Pregunta: {self.texto}")
        if not self.respuestas:
            print("No hay respuestas guardadas")
        else:
            print("Respuestas:")
            for i in range(len(self.respuestas)):
                print(f"{i + 1}. {self.respuestas[i]}")
        
class PreguntasOpcionMultiple(Pregunta):
    def _init_(self, texto, opciones):
        super()._init_(texto)
        self.opciones = opciones

    def registrar_respuesta(self, indice):
        if 0 <= indice < len(self.opciones):
            self.respuestas.append(self.opciones[indice])
        else:
            print("Opcion no encontrada")