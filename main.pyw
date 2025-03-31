#Biblioteca para Interfaces Graficas
from tkinter import *
import utils

#Variables
Archive = ""
informacion = open("informacion.txt")

raiz=Tk()

raiz.title("AIEvaluation")
raiz.geometry("800x600")
raiz.resizable(False, False)
myFrame = Frame(raiz)

myFrame.config(bg="#121212")
myFrame.pack(fill="both", expand="True") 
myFrame.config(width="1400", height="900")

#Buscador
nameArchive = Entry(myFrame, font=("Arial", 15))
nameArchive.place(x=205, y=24, width=259, height=36)

examLabel = Label(myFrame, text="Exam", fg="white", font=("Arial",16))
examLabel.config(bg="#121212")
examLabel.place(x=40, y=71)

#En esta parte es donde se vera o introducira el examen
exam = Text(myFrame, width=70, height=40)
exam.place(x=40, y=111, width=555, height=458)

def GetAnalize():
    global informacion

#Boton para Analizar el examen
analize = Button(myFrame, text="Analize", fg="white", font=("Arial", 20), command=GetAnalize)
analize.config(bg="#1E90FF")
analize.place(x=622, y=419, width=151, height=46)

#Obtener el nombre del archivo para su lectura
def GetNameArchive():
    global Archive
    Archive = nameArchive.get()
    text = open(Archive)
    exam.insert(INSERT, text.read())

getArchive = Button(myFrame, text="Archive", command=GetNameArchive, fg="white", font=("Arial", 15))
getArchive.config(bg="#1E90FF")
getArchive.place(x=464, y=24, width=131, height=36)

score=0

#Resultado de la evaluacion
scoreLabel = Label(myFrame, text="Score", fg="white", font=("Arial", 40))
scoreLabel.place(x=623, y=135)
scoreLabel.config(bg="#121212")
showScore = Label(myFrame, text=str(score)+"%", fg="#1E90FF", font=("Arial", 40))
showScore.place(x=669, y=221)
showScore.config(bg="#121212")

raiz.mainloop()
