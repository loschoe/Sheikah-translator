
# Chargement du module tkinter
from tkinter import * # pour Python2 ce serait Tkinter


# Construction de la fenêtre principale «window»
window = Tk()
window.title('Language Sheika')
window.geometry("1080x720")

# Construction d'un simple bouton
qb = Button(window, text='Bravo Louis !', command=window.quit)
qb.place (x=100, y=0) 

# Placement du bouton dans «window»
qb.pack()

txt1=Label(window, text='Saisie manuscrite : ')
txt2=Label(window, text='Traduction en Sheikah : ')
entr1=Entry(window, bg='white')
entr2=Entry(window, bg='white')
txt1.grid(row=0)
txt2.grid(row=1)
entr1.grid(row=0, column=1)
entr2.grid(row=1, column=1)

window.geometry("1080x720")
qb = Button(window, text='Bravo Louis !', command=window.quit)
window.mainloop()

def alert():
    showinfo("alerte", "Bravo!")

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)