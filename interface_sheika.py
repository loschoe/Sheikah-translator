
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


