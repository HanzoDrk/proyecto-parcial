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
    
    def mostrar_resultado(self):
        print(f"Pregunta de Opcion multiple: {self.texto}\nOpciones:")
        for i in range(len(self.opciones)):
            print(f"{i + 1}. {self.opciones[i]}")
        super().mostrar_resultado()

class PreguntaTextoLibre(Pregunta):
    def registrar_respuesta(self, texto):
        self.texto.append(texto)

    def mostrar_resultado(self):
        print(f"Pregunta de texto libre: {self.texto}")
        return super().mostrar_resultado()

class Encuesta:
    def _init_(self, titulo):
        self.titulo = titulo
        self.preguntas = []

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def mostrar_preguntas(self):
        print(f"Encuesta: {self.titulo}\nPreguntas:")
        for i in range(len(self.preguntas)):
           print(f"{i + 1}. {self.preguntas[i]}")

    def responder_encuesta(self):
        print(f"== Encuensta: {self.titulo} ==")
        for preguntas in self.preguntas:
            if isinstance(preguntas, PreguntasOpcionMultiple):
                print(f"------\n{preguntas.texto}")
