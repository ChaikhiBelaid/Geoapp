from tkinter import *
 #Créer la 1 fenetre :
window=Tk()
 #personnalier la fenetre :
window.title("GEO Application")
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap("logo.ico")
window.config(background="#41B77F")
#Créer un frame (boite):
frame=Frame(window, bg="#41B77F", bd=1, relief=SUNKEN)
#Ajouter texte :
label_title=Label(frame, text="Bienvenue sur GEO App", font=("Courrier",40),bg="#41B77F", fg='white')
label_title.pack(expand=YES)
#ajouter autre texte : 
label_subtitle=Label(frame, text="Une application qui vous garantit une meilleur gestion de stock", font=("Courrier",25),bg="#41B77F", fg='white')
label_subtitle.pack(expand=YES)
#Ajouter la boite (frame):
frame.pack(expand=YES)
#Création d'une barre menu :
menu_barre = Menu(window)
#créer un premier menu : 
file_menu = Menu(menu_barre, tearoff=0)
"""file_menu.add_command(label="Nouveau",command="#")"""
file_menu.add_command(label="quitter",command=window.quit)
menu_barre.add_cascade(label="Fichier", menu=file_menu)
#configurer window pour ajouter ce menu :
window.config(menu=menu_barre)
#afficher la fenétre :
window.mainloop()