class Pregunta:  # Clase Principal, plantilla para cualquier tipo de pregunta
    def __init__(self, texto):
        self.texto = texto
        self.respuestas = []

    def registrar_respuesta(self, respuesta):  # Metodo donde se registrar respuestas 
        self.respuestas.append(respuesta)

    def mostrar_resultados(self):  # Imprime el texto de la pregunta y las respuestas guardadas
        print(f"Pregunta: {self.texto}")
        if not self.respuestas:
            print("No hay respuestas guardadas")
        else:
            print("Respuestas:")
            for i in range(len(self.respuestas)):
                print(f"{i + 1}. {self.respuestas[i]}")


# Clase hija dedicada a preguntas con opciones
class PreguntasOpcionMultiple(Pregunta): 
    def __init__(self, texto, opciones):
        super().__init__(texto)  
        self.opciones = opciones

    def registrar_respuesta(self, indice):
        if 0 <= indice < len(self.opciones):
            self.respuestas.append(self.opciones[indice])
        else:
            print("Opción no encontrada")
    
    def mostrar_resultados(self):
        print(f"Pregunta de Opción múltiple: {self.texto}\nOpciones:")
        for i in range(len(self.opciones)):
            print(f"{i + 1}. {self.opciones[i]}")
        super().mostrar_resultados()


# Clase hija para preguntas con respuesta de texto
class PreguntaTextoLibre(Pregunta):
    def registrar_respuesta(self, texto):
        self.respuestas.append(texto)

    def mostrar_resultados(self):
        print(f"Pregunta de texto libre: {self.texto}")
        super().mostrar_resultados()


# Clase Encuesta
class Encuesta:
    def __init__(self, titulo):
        self.titulo = titulo
        self.preguntas = []

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def mostrar_preguntas(self):
        print(f"Encuesta: {self.titulo}\nPreguntas:")
        for i in range(len(self.preguntas)):
            print(f"{i + 1}. {self.preguntas[i]}")

    def responder_encuesta(self):
        print(f"== Encuesta: {self.titulo} ==")
        for preguntas in self.preguntas:
            match preguntas:
                case PreguntasOpcionMultiple():
                    print(f"------\n{preguntas.texto}")
                    for i in range(len(preguntas.opciones)):
                        print(f"{i + 1}. {preguntas.opciones[i]}")
                    try:
                        eleccion = int(input("Seleccione una opción: ")) - 1
                        preguntas.registrar_respuesta(eleccion)
                    except ValueError:
                        print("Error. Entrada inválida, seleccione una opción.")
                case PreguntaTextoLibre():
                    respuesta = input(f"{preguntas.texto}\nRespuesta: ")
                    preguntas.registrar_respuesta(respuesta)

    def mostrar_resultados(self):
        print(f"=== Resultados de la Encuesta {self.titulo} ===")
        for preguntas in self.preguntas:
            preguntas.mostrar_resultados()


# Clase Sistema
class Sistema:
    def __init__(self):
        self.encuestas = []
            
    def crear_encuesta(self):
        titulo = input("Título de la encuesta: ")
        encuesta = Encuesta(titulo)

        while True:
            print("== Tipo de Preguntas ==")
            tipo = input("0. Salir | 1. Opción Múltiple | 2. Texto Libre\n")

            match tipo:
                case "1":
                    texto = input("Escriba la Pregunta: ")
                    opciones = []
                    while True:
                        opcion = input("Agregue una opción <<Escriba 0 para terminar>>: ")
                        if opcion == "0":
                            break
                        opciones.append(opcion)
                    encuesta.agregar_pregunta(PreguntasOpcionMultiple(texto, opciones))

                case "2":
                    texto = input("Escriba la Pregunta: ")
                    encuesta.agregar_pregunta(PreguntaTextoLibre(texto))

                case "0":
                    break

                case _:
                    print("Opción no válida. Seleccione una de las 3 opciones.")

        self.encuestas.append(encuesta)
        print("Encuesta Creada :D")
        
    def responder_encuesta(self):
        if not self.encuestas:
            print("No hay encuestas")
            return
        self.mostrar_encuestas()
        inx = int(input("Seleccione una encuesta: ")) - 1
        self.encuestas[inx].responder_encuesta()

    def mostrar_resultados(self):
        if not self.encuestas:
            print("No hay encuestas para mostrar")
            return
        self.mostrar_encuestas()
        inx = int(input("Seleccione una encuesta: ")) - 1
        self.encuestas[inx].mostrar_resultados()

    def mostrar_encuestas(self):
        print(f"=== Encuestas Disponibles ===")
        for i in range(len(self.encuestas)):
            print(f"{i + 1}. {self.encuestas[i].titulo}")

    def menu(self):
        while True:
            print("\n=-= Sistema de Encuestas =-=\n0. Salir\n1. Crear encuesta\n2. Responder encuesta\n3. Mostrar resultado")
            opciones = input("Seleccione una opción: ")

            match opciones:
                case "1":
                    self.crear_encuesta()
                case "2":
                    self.responder_encuesta()
                case "3":
                    self.mostrar_resultados() 
                case "0":
                    print("\nSaliendo del sistema de encuestas. ¡Adiós!")
                    break
                case _:
                    print("Seleccione una opción válida del sistema de encuestas.")


p = Sistema()
p.menu()

''' Errores al tratar de ejecutarlo. 
problema con los constructores. los tenia asi = _init_. 
Error al unificar el nombres de los metodos, use metodos en singular y plural '''