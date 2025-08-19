class Pregunta:  #Clase Principal, plantilla para cualquier tipo de pregunta
    def __init__(self, texto):
        self.texto = texto
        self.respuestas = []

    def registrar_respuesta(self, respuesta): #Metodo donde se registrar respuesas 
        self.respuestas.append(respuesta) #Agrega las prespuestas a la lista self.respuestas

    def mostrar_resultados(self): #Imprime el texto de la pregunta y las respuestas guardadas
        print(f"Pregunta: {self.texto}")
        if self.respuestas: #Si hay respuestas, se imprimen
            print("Respuestas:")
            # Uso de enumerate para imprimir con índice en lugar de range(len(...))
            for i, r in enumerate(self.respuestas, start=1):
                print(f"{i}. {r}")
        else: #Si no encuentra respuestas imprime lo de abajo
            print("No hay respuestas guardadas")


#Calse hijas dedicada a realizar solo preguntas con opciones.      
class PreguntasOpcionMultiple(Pregunta): 
    def __init__(self, texto, opciones):
        super().__init__(texto)   #Corregido constructor __init__
        self.opciones = opciones

    def registrar_respuesta(self, indice): #Metodo para registrar la respuesta seleccionada
        if 0 <= indice < len(self.opciones): #Validar que el índice exista
            self.respuestas.append(self.opciones[indice])
        else:
            print("Opción no encontrada")
    
    def mostrar_resultados(self): #Muestra la pregunta y sus opciones
        print(f"Pregunta de Opción múltiple: {self.texto}\nOpciones:")
        # Uso de enumerate para recorrer las opciones con índice automático
        for i, opcion in enumerate(self.opciones, start=1):
            print(f"{i}. {opcion}")
        super().mostrar_resultados()


#Calses Hijas para realizar solo preguntas con respuesta de texto.
class PreguntaTextoLibre(Pregunta):
    def registrar_respuesta(self, texto): #Metodo para guardar la respuesta escrita
        self.respuestas.append(texto)

    def mostrar_resultados(self): #Muestra la pregunta y las respuestas
        print(f"Pregunta de texto libre: {self.texto}")
        super().mostrar_resultados()


#Clase Encuesta, Muestra las preguntas, permite agregar preguntas y responder. Encargado del flujo de la encuesta
class Encuesta:
    def __init__(self, titulo):
        self.titulo = titulo
        self.preguntas = []

    def agregar_pregunta(self, pregunta): #Metodo para agregar preguntas
        self.preguntas.append(pregunta)

    def mostrar_preguntas(self): #Muestra todas las preguntas de la encuesta
        print(f"Encuesta: {self.titulo}\nPreguntas:")
        # enumerate en lugar de range(len(...)) para listar preguntas
        for i, p in enumerate(self.preguntas, start=1):
            print(f"{i}. {p}")

    def responder_encuesta(self): #Permite responder todas las preguntas
        print(f"== Encuesta: {self.titulo} ==")
        for preguntas in self.preguntas:
            match preguntas:
                case PreguntasOpcionMultiple(): #Si la pregunta es de opción múltiple
                    print(f"------\n{preguntas.texto}")
                    # enumerate para imprimir todas las opciones con su número
                    for i, opcion in enumerate(preguntas.opciones, start=1):
                        print(f"{i}. {opcion}")
                    try:
                        eleccion = int(input("Seleccione una opción: ")) - 1
                        preguntas.registrar_respuesta(eleccion)
                    except ValueError:
                        print("Error. Entrada inválida, seleccione una opción.")
                case PreguntaTextoLibre(): #Si la pregunta es de texto libre
                    respuesta = input(f"{preguntas.texto}\nRespuesta: ")
                    preguntas.registrar_respuesta(respuesta)

    def mostrar_resultados(self): #Muestra los resultados de todas las preguntas
        print(f"=== Resultados de la Encuesta {self.titulo} ===")
        for preguntas in self.preguntas:
            preguntas.mostrar_resultados()


#Perimite crear las encuestas, administrarlas y es el encargado de mostrastrar el menu.
class Sistema:
    def __init__(self):
        self.encuestas = []
            
    def crear_encuesta(self): #Metodo para crear una nueva encuesta
        titulo = input("Título de la encuesta: ")
        encuesta = Encuesta(titulo)

        while True:
            print("== Tipo de Preguntas ==")
            tipo = input("0. Salir | 1. Opción Múltiple | 2. Texto Libre\n")

            match tipo:
                case "1": #Crear pregunta de opción múltiple
                    texto = input("Escriba la Pregunta: ")
                    opciones = []
                    while True:
                        opcion = input("Agregue una opción <<Escriba 0 para terminar>>: ")
                        if opcion == "0":
                            break
                        opciones.append(opcion)
                    encuesta.agregar_pregunta(PreguntasOpcionMultiple(texto, opciones))

                case "2": #Crear pregunta de texto libre
                    texto = input("Escriba la Pregunta: ")
                    encuesta.agregar_pregunta(PreguntaTextoLibre(texto))

                case "0": #Salir del bucle
                    break

                case _: #Si el usuario selecciona algo inválido
                    print("Opción no válida. Seleccione una de las 3 opciones.")

        self.encuestas.append(encuesta)
        print("Encuesta Creada :D")
        
    def responder_encuesta(self): #Permite responder una encuesta seleccionada
        if not self.encuestas: #Validar si existen encuestas
            print("No hay encuestas")
            return
        self.mostrar_encuestas()
        inx = int(input("Seleccione una encuesta: ")) - 1
        self.encuestas[inx].responder_encuesta()

    def mostrar_resultados(self): #Muestra los resultados de una encuesta seleccionada
        if not self.encuestas: #Validar si existen encuestas
            print("No hay encuestas para mostrar")
            return
        self.mostrar_encuestas()
        inx = int(input("Seleccione una encuesta: ")) - 1
        self.encuestas[inx].mostrar_resultados()

    def mostrar_encuestas(self): #Lista todas las encuestas creadas
        print(f"=== Encuestas Disponibles ===")
        # Uso de enumerate para mostrar el índice y el título de cada encuesta
        for i, encuesta in enumerate(self.encuestas, start=1):
            print(f"{i}. {encuesta.titulo}")

    def menu(self): #Menú principal del sistema
        while True:
            print("\n=-= Sistema de Encuestas =-=\n0. Salir\n1. Crear encuesta\n2. Responder encuesta\n3. Mostrar resultado")
            opciones = input("Seleccione una opción: ")

            match opciones:
                case "1": #Crear encuesta
                    self.crear_encuesta()
                case "2": #Responder encuesta
                    self.responder_encuesta()
                case "3": #Mostrar resultados
                    self.mostrar_resultados()
                case "0": #Salir del sistema
                    print("\nSaliendo del sistema de encuestas. ¡Adiós!")
                    break
                case _: #Opción inválida
                    print("Seleccione una opción válida del sistema de encuestas.")


p = Sistema()
p.menu()


''' Errores al tratar de ejecutarlo. 
problema con los constructores. los tenia asi = _init_. 
Error al unificar el nombres de los metodos, use metodos en singular y plural '''