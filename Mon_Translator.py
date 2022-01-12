
# Importation du module Tkinter
from tkinter import*
# importation du module webbrowser afin d'afficher les sites webs 
import webbrowser 

# Déf des variables pour ouvrir les tutos
def oppen_graven_tuto():
	webbrowser.open_new("https://www.youtube.com/watch?v=N4M4W7JPOL4")
def oppen_second_tuto():
	webbrowser.open_new("https://info.blaisepascal.fr/tkinter")
def oppen_tres_tuto():
	webbrowser.open_new("https://python.doctor/page-tkinter-interface-graphique-python-tutoriel") 

# def de la fonction events pour les lettres 
## pas fini##
def lettre_a(event):
	print ("test")
# Faire les autres events et pas fini 



# créer la fenetre 
window = Tk()

#personaliser la fenetre 
window.title ("Interface de Graven")
window.geometry("1080x720")
window.minsize(480, 360)
window.config (background= 'darkgreen')


# creation de la frame
# masquer pour utiliser le cadrillage 
#frame = Frame(window, bg= 'darkblue', bd=0)
#tree = ttk.Treeview(frame, columns = (1,2,3), height = 5, show = "headings")
#tree.pack(side = 'left')



# ajouter un premier text à la fenetre "titre"
# Alligné !!
label_title = Label (window, text="Bienvenue sur le translator", font=("Arial", 30), bg= 'darkgreen', fg= 'white')  
label_title.grid(row=0, column=3 , sticky=N)

# ajouter un second text à la fenetre "texte"
# Alligné !!
label_subtitle = Label (window, text="Découvre comment il fonctionne et traduit tes messages en Sheikah", font=("Arial", 15), bg= 'darkgreen', fg= 'white')  
label_subtitle.grid(row=2, column=3, sticky=N)

# ajouter un permier bouton "Aides au codage"
# Alligné !!
yt_bouton= Button(text="Aides au codage", font=("Arial", 15), bg= 'white', fg= 'darkgreen', command=lambda:[oppen_graven_tuto(), oppen_second_tuto(), oppen_tres_tuto()]) 
yt_bouton.grid(row=0, column=2, sticky=W)

# ajouter un bouton pour "fermer la page" 
# Alligné !!
quit_bouton = Button(text="Fermer", font=("Arial", 15), bg= 'white', fg= 'darkgreen', command=window.quit)  
quit_bouton.grid(row=0, column=1, sticky=W)

# ajouter de la zone de text 
# Alligné !!
text_fr = Text(window, width=40, height=4, font=("Arial", 20))
text_fr.grid(row=10, column=3, sticky=N)

# Création du bouton "Traduire "
### JE VOUDRAIS L'ESPACER !!!!!!
trad_bouton = Button(window, text="Traduire", font=("Arial", 25), bg= 'white', fg= 'darkgreen')
trad_bouton.grid(row=12, column= 3, sticky=N)



# afficher la frame
#frame.grid(row=13, column=3, sticky=N)

# afficher la fenetre
window.mainloop()

