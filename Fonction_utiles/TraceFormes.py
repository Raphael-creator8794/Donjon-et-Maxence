# Petit exercice utilisant la bibliothèque graphique tkinter
from tkinter import *
from random import randrange


# --- définition des fonctions gestionnaires d'événements : ---
def dessinerForme():
  "Tracé d'une ligne dans le canevas can1"
  global x1, y1, x2, y2, coul, forme
  if forme == 1 :
    can1.create_line(x1,y1,x2,y2,width=2,fill=coul)
  elif forme == 2 :
    can1.create_oval(x1,y1,x2,y2,width=2,fill=coul)
  elif forme == 3 :
    can1.create_rectangle(x1,y1,x2,y2,width=2,fill=coul)
  elif forme == 4 :
    can1.create_arc(x1,y1,x2,y2,width=2,fill=coul)
  elif forme == 5 :
    #pour dessiner un triangle
    can1.create_polygon(x1,y1,x2,y2, x1+x2, y1+y2, width=2,fill=coul)

# modification des coordonnées pour la ligne suivante :
  y2, y1 = y2+10, y1-10

def effacer() :
  can1.delete('all')

def changerCouleur():
  "Changement aléatoire de la couleur du tracé"
  global coul
  pal=['#8ada76','#3ac0b4','#3a4ac0','#46c03a','#7d3ac0','#e768df','#9f1d58','#dce12c']
  c = randrange(8)
  coul = pal[c]

def changerForme():
  global forme
  forme = randrange(6)
  

#------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
x1, y1, x2, y2 = 10, 290, 290, 10

# coordonnées de la ligne
coul = '#8ada76'
forme = 1
# couleur de la ligne
# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Tracer des formes")
#fen1.iconbitmap("img/logo.ico")
# création des widgets "esclaves" :
can1 = Canvas(fen1,bg='#8f9a88',height=300,width=300)
can1.pack(side=LEFT)
bt1 = Button(fen1,text='Quitter',command=fen1.destroy) # destruction (fermeture) de la fenêtre
bt1.pack(side=BOTTOM)
bt2 = Button(fen1,text='Tracer une forme', bg="blue", fg="white", font=("Calibri", 12),width=15, height=2,command=dessinerForme)
bt2.pack()
bt3 = Button(fen1,text='Changer la couleur',bg="#c276da", fg="white", font=("Calibri", 12),width=15, height=2,command=changerCouleur)
bt3.pack()
bt4 = Button(fen1,text='Changer la forme',bg="#76dad8", fg="white", font=("Calibri", 12),width=15, height=2,command=changerForme)
bt4.pack()
bt5 = Button(fen1,text='Effacer',bg="#124662", fg="white", font=("Calibri", 12),width=15, height=2,command=effacer)
bt5.pack()
fen1.mainloop() # démarrage du réceptionnaire d’événements
