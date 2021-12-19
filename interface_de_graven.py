<<<<<<< HEAD

# Importation du module Tkinter
from tkinter import *
# importation du module webbrowser afin d'afficher les sites webs 
import webbrowser 

# Déf de la variable pour ouvrir les tutos
def oppen_graven_tuto():
	webbrowser.open_new("https://www.youtube.com/watch?v=N4M4W7JPOL4")

def oppen_second_tuto():
	webbrowser.open_new("https://info.blaisepascal.fr/tkinter")

def oppen_tres_tuto():
	webbrowser.open_new("https://python.doctor/page-tkinter-interface-graphique-python-tutoriel") 

# créer une fenetre 
window = Tk()

#personaliser la fenetre 
window.title ("Interface de Graven")
window.geometry("1080x720")
window.minsize(480, 360)
window.config (background= 'darkgreen')

# ajouter un premier text à la fenetre
label_title = Label (window, text="Bienvenue sur le translator", font=("Arial", 30), bg= 'darkgreen', fg= 'white')  
label_title.pack()

# ajouter un second text à la fenetre
label_subtitle = Label (window, text="Découvre comment il fonctionne et traduit tes messages en Sheikah", font=("Arial", 15), bg= 'darkgreen', fg= 'white')  
label_subtitle.pack()

# ajouter un permier bouton qui ouvre des pages webs 
yt_bouton= Button(text="Aides au codage", font=("Arial", 30), bg= 'white', fg= 'darkgreen', command=lambda:[oppen_graven_tuto(), oppen_second_tuto(), oppen_tres_tuto()]) 
yt_bouton.pack()

# ajouter un bouton pour fermer la page 

qb = Button(window, text="Fermer", font=("Arial", 30), bg= 'white', fg= 'darkgreen', command=window.quit)
qb.place (x=100, y=0) 

# Affichage du bouton dans «window»
qb.pack()


# afficher 
window.mainloop()



























































=======

from tkinter import *
import webbrowser 

def oppen_graven_tuto():
	webbrowser.open_new("https://www.youtube.com/watch?v=N4M4W7JPOL4")
 	 

# créer une fenetre 
window = Tk()

#personaliser la fenetre 
window.title ("Interface de Graven")
window.geometry("1080x720")
window.minsize(480, 360)
window.config (background= 'darkgreen')
root = tk.Tk()
root.geometry("200x200")

root.iconphoto(False, tk.PhotoImage(file='C:\Users\loschoe\Desktop\logozelda.png'))

root.mainloop()

# ajouter un premier text à la fenetre
label_title = Label (window, text="Bienvenue sur le translator", font=("Arial", 30), bg= 'darkgreen', fg= 'white')  
label_title.pack()

# ajouter un second text à la fenetre
label_subtitle = Label (window, text="Découvre comment il fonctionne et traduit tes messages en Sheikah", font=("Arial", 15), bg= 'darkgreen', fg= 'white')  
label_subtitle.pack()

# ajouter un permier bouton
yt_bouton= Button(text="Ouvrir le tuto de Graven", font=("Arial", 30), bg= 'white', fg= 'darkgreen', command=oppen_graven_tuto) 
yt_bouton.pack()
# afficher 
window.mainloop()
>>>>>>> d798fa54647119f763129ee3be80f51b85d1087a
