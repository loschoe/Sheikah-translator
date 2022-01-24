
# Importation du module Tkinter
from tkinter import*
import tkinter as tk
# importation du module webbrowser afin d'afficher les sites webs 
import webbrowser 

# Définition des variables pour ouvrir les tutos
def oppen_graven_tuto():
	webbrowser.open_new("https://www.youtube.com/watch?v=N4M4W7JPOL4")
def oppen_second_tuto():
	webbrowser.open_new("https://info.blaisepascal.fr/tkinter")
def oppen_tres_tuto():
	webbrowser.open_new("https://python.doctor/page-tkinter-interface-graphique-python-tutoriel") 

# Définition de la reconnaissance des lettres 
def getEntry():
    Detection = myEntry.get()
    maListe=[i for i in Detection]
    print (maListe)
    # LE PRINT maListe C'est juste pour le test !!

# création de la fenetre (window) 
window = Tk()

#personalisation de la fenetre (window) 
window.title ("Translator Sheikah")
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap('logo.ico')
window.config (background= 'darkgreen')
#window.config(bg=PhotoImage(file='Le_fond.jpg'))

# creation de la frame (INNUTILE PUISQUE J'UTILISE .GRID)
#############################################################################
#frame = Frame(window, bg= 'darkblue', bd=0)
#tree = ttk.Treeview(frame, columns = (1,2,3), height = 5, show = "headings")
#tree.pack(side = 'left')
#############################################################################
# AFFICHER UNE IMAGE A REVOIR !!!!

#photo = PhotoImage(file='lettre-B.gif')
#Canevas = Canvas(window)                 
#Canevas.config(height=photo.height(),width=photo.width())   
#Canevas.create_image(300 ,100, anchor=W,image=photo)              
#Canevas.grid(row=35, pady=25, columnspan=2, sticky=W)

# Code pour image de la lettre A
############################################################################
# PAS FONCTIONNEL #

#width = 15
#height = 15

#image = PhotoImage(file='A.png')
#canvas = Canvas(window, width=width, height=height, bg='darkgreen'
#canvas.create_image(image)
#canvas.grid(row=35, column=2, sticky=W)
############################################################################

# ajouter le "titre" de la fenetre (window)
# Alligné !!
label_title = Label (window, text="Bienvenue sur le translator", font=("Arial", 30), bg= 'darkgreen', fg= 'white')  
label_title.grid(row=0, column=3 , sticky=N)
############################################################################

# ajouter d'un "texte" à la fenetre (window)
# Alligné !!
label_subtitle = Label (window, text="Découvre comment il fonctionne et traduit tes messages en Sheikah", font=("Arial", 15), bg= 'darkgreen', fg= 'white')  
label_subtitle.grid(row=2, column=3, sticky=N)
############################################################################

# ajouter le bouton "Aides au codage" à la fenetre (window)
# Alligné !!
yt_bouton= Button(text="Aides au codage", font=("Arial", 15), bg= 'white', fg= 'darkgreen', command=lambda:[oppen_graven_tuto(), oppen_second_tuto(), oppen_tres_tuto()]) 
yt_bouton.grid(row=0, column=2, sticky=W)
############################################################################

# ajouter le bouton pour "fermer la page" à la fenetre (window)
# Alligné !!
quit_bouton = Button(text="Fermer", font=("Arial", 15), bg= 'white', fg= 'darkgreen', command=window.quit)  
quit_bouton.grid(row=0, column=1, sticky=W)
############################################################################

# ajouter de la "zone de texte" à la fenetre (window) 
# Alligné !!
myEntry = Entry(window, width=40, font=("Arial", 20))
myEntry.grid(row=10, column=3, sticky=N)
#height=4, 
# ###########################################################################

# ajouter lu bouton "Traduire " à la fenetre (window)
# Alligné !!
trad_bouton = Button(window, text="Traduire", font=("Arial", 25), bg= 'white', fg= 'darkgreen', relief= 'raised', command=getEntry)
trad_bouton.grid(row=30, pady=20, column= 3, sticky=N)
############################################################################

# afficher la frame
#frame.grid(row=13, column=3, sticky=N)
############################################################################
# afficher la fenetre (window)
window.mainloop()


