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

#Clase Encuesta, Muestra las preguntas, permite agregar preguntas y responder. Encargado del flujo de la encuesta
class Encuesta:
    def __init__(self, titulo):
        self.titulo = titulo
        self.preguntas = []

    def agregar_pregunta(self, pregunta): #Metodo para agregar preguntas
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
                for i in range(len(preguntas.opciones)): #cambie el metodo ya que recorria el texto
                    print(f"{i + 1}. {preguntas.opciones[i]}") #lo mismo, cambie texto por opciones
                try:
                    eleccion = int(input("Seleccione una opcion: ")) -1
                    preguntas.registrar_respuesta(eleccion)
                except ValueError:
                    print("Error. entrada invalida seleccione una opcion.")
            elif isinstance(preguntas, PreguntaTextoLibre):
                respuesta = input(f"{preguntas.texto}\nRespuesta: ")
                preguntas.registrar_respuesta(respuesta)

    def mostrar_resultados(self):
        #Simplemente un separador
        print(f"=== Resultados de la Encuesta {self.titulo} ===")
        for preguntas in self.preguntas:
            preguntas.mostrar_resultados()

#Perimite crear las encuestas, administrarlas y es el encargado de mostrastrar el menu.
class Sistema:
    def __init__(self):
        self.encuestas = []
            
    def crear_encuesta(self):
        titulo = input("Titulo de la encuesta: ")
        encuesta = Encuesta(titulo)

        while True:
            print("== Tipo de Preguntas ==")
            tipo = input("0. Salir | 1. Opcion Multiple | 2. Texto Libre\n")
            if tipo == "1":
                texto = input("Escriba la Pregunta: ")
                opciones = []
                while True:
                    opcion = input("Agrege una opcion <<Escriba 0 para terminar>>: ")
                    if opcion == "0":
                        break
                    opciones.append(opcion)
                encuesta.agregar_pregunta(PreguntasOpcionMultiple(texto, opciones))
                print("------")

            elif tipo == "2":
                texto = input("Escriba la Pregunta: ")
                encuesta.agregar_pregunta(PreguntaTextoLibre(texto))
                print("------")

            elif tipo == "0": #Me falto agregar la opcion de salir del bucle
                break 
            else:
                print("Opcion no valida. Seleccione una de las 3 opciones.")

        #movi estas dos lineas un espacio para atras ya que se ejecutava todas las veces que se crea una pregunta y no solo una vez.
        print("------")
        self.encuestas.append(encuesta)
        print("Encuesta Creada :D")
        
    def responder_encuesta(self):
        if not self.encuestas:
            print("No hay encuestas")
            return
        self.mostrar_encuestas()
        while True:
            try:
                inx = int(input("Seleccione una encuesa: "))-1
                if 0 <= inx < len(self.encuestas):
                    self.encuestas[inx].responder_encuesta()
                    break
                else:
                    print("La opcion que intenta elegir no existe.")
            except ValueError:
                print("Entrada invalida. Por favor, ingrese un numero.")

    def mostrar_resultados(self):
        if not self.encuestas:
            print("No hay encustas para mostrar")
            return
        self.mostrar_encuestas()

        while True:
            try:
                inx = int(input("Seleccione una encuesa: "))-1
                if 0 <= inx < len(self.encuestas):
                    self.encuestas[inx].mostrar_resultados()
                    break
                else:
                    print("La opcion que intenta elegir no existe.")
            except ValueError:
                print("Ingrese un numero valido.")

    def mostrar_encuestas(self):
        print(f"=== Encuestas Disponibles ===")
        for i in range(len(self.encuestas)):
            print(f"{i + 1}. {self.encuestas[i].titulo}")

    def menu(self):
        while True:
            print("\n=-= Sistema de Encuestas =-=\n0. Salir\n1. Crear encuesta\n2. Responder encuesta\n3. Mostrar resultado")
            opciones = input("selecione una opcion: ")

            if opciones == "1":
                self.crear_encuesta()
            elif opciones == "2":
                self.responder_encuesta()
            elif opciones == "3":
                self.mostrar_resultados()
                #El metodo esta mal escrito, ya que es con s"
                #Seria mostrar_resultados()
            elif opciones == "0":
                print("\nSaliendo del sistema de encuestas. Adios!!!")
                break
            else:
                print("Seleccione una opcion del sistema de encuestas.")

p = Sistema()
p.menu()

'''
Errores al tratar de ejecutarlo.
problema con los constructores. los tenia asi = _init_.
Error al unificar el nombres de los metodos, use metodos en singular y plural
'''