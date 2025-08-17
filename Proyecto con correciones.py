class Pregunta: #Clase Principal, plantilla para cualquier tipo de pregunta
    def __init__(self, texto):
        self.texto = texto
        self.respuestas = []

    def registrar_respuesta(self, respuesta): #Metodo donde se registrar respuesas 
        self.respuestas.append(respuesta) #Agrega las prespuestas a la lista slef.repuestas

    def mostrar_resultados(self): #Imprimer el texto de la pregunta y las respuestas guardadas
        print(f"Pregunta: {self.texto}")
        if not self.respuestas: #Si no ecuentra respuestas imprime lo de abajo
            print("No hay respuestas guardadas")
        else:
            print("Respuestas:")
            for i in range(len(self.respuestas)): #recorre la lista de respuestas para imprimirlas.
                print(f"{i + 1}. {self.respuestas[i]}")

#Calse hijas dedicada a realizar solo preguntas con opciones.      
class PreguntasOpcionMultiple(Pregunta): 
    def __init__(self, texto, opciones):
        super().__init__(texto)
        #El constructor siempre lleva doble guion bajo.
        #super().__init__(texto)
        self.opciones = opciones

    def registrar_respuesta(self, indice):
        if 0 <= indice < len(self.opciones):
            self.respuestas.append(self.opciones[indice])
        else:
            print("Opcion no encontrada")
    
    def mostrar_resultados(self):
        print(f"Pregunta de Opcion multiple: {self.texto}\nOpciones:")
        for i in range(len(self.opciones)):
            print(f"{i + 1}. {self.opciones[i]}")
        super().mostrar_resultados()

#Calses Hijas para realizar solo preguntas con respuesta de texto.
class PreguntaTextoLibre(Pregunta):
    def registrar_respuesta(self, texto):
        self.respuestas.append(texto) #corregi esto ya que me da un erro y crashea. ver con los anteriores commits

    def mostrar_resultados(self):
        print(f"Pregunta de texto libre: {self.texto}")
        super().mostrar_resultados()