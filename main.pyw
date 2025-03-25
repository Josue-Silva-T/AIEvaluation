#Biblioteca para Interfaces Graficas
from tkinter import *

#Variables
Archive = ""

raiz=Tk()

raiz.title("AIEvaluation")
raiz.geometry("1400x900")
raiz.resizable(False, False)
myFrame = Frame(raiz)

myFrame.config(bg="#121212")
myFrame.pack(fill="both", expand="True") 
myFrame.config(width="1400", height="900")

#Buscador
nameArchive = Entry(myFrame, font=("Arial", 15))
nameArchive.place(x=494, y=41, width=259, height=36)

examLabel = Label(myFrame, text="Exam", fg="white", font=("Arial",20))
examLabel.config(bg="#121212")
examLabel.place(x=50, y=128)

resultLabel = Label(myFrame, text="Result", fg="white", font=("Arial",20))
resultLabel.config(bg="#121212")
resultLabel.place(x=846, y=128)

#En esta parte es donde se vera o introducira el examen
exam = Text(myFrame, width=70, height=40)
exam.place(x=40, y=160, width=502, height=680)

#En esta parte se mostraran los resultados
result = Text(myFrame, width=70, height=40)
result.place(x=836, y=160, width=502, height=680)

#Boton para Analizar el examen
analize = Button(myFrame, text="Analize", fg="white", font=("Arial", 20))
analize.config(bg="#1E90FF")
analize.place(x=613, y=450, width=151, height=46)

#Obtener el nombre del archivo para su lectura
def GetNameArchive():
    global Archive
    Archive = nameArchive.get()

getArchive = Button(myFrame, text="Archive", command=GetNameArchive, fg="white", font=("Arial", 15))
getArchive.config(bg="#1E90FF")
getArchive.place(x=753, y=41, width=131, height=36)

score=0

#Resultado de la evaluacion
scoreLabel = Label(myFrame, text="Score", fg="white", font=("Arial", 40))
scoreLabel.place(x=634, y=166)
scoreLabel.config(bg="#121212")
showScore = Label(myFrame, text=str(score)+"%", fg="#1E90FF", font=("Arial", 40))
showScore.place(x=660, y=252)
showScore.config(bg="#121212")

raiz.mainloop()
