from tkinter import *
import xlrd
import datetime
import time
from time import strftime
from tkinter import messagebox
#import xlwt
#ouvrir les textes :
entre_stock=open("stock_entre.txt","r")
sortie_stock=open("stock_sortie.txt", "r")
entre1=open("entre1.txt", "r")
sortie1=open("sortie1.txt", "r")
entre2=open("entre2.txt", "r")
sortie2=open("sortie2.txt", "r")
#Entrée de stock : 
codes_texte_entre_stock=entre_stock.readlines()
codes_barre_entre_stock=[]
for i in range(len(codes_texte_entre_stock)-1):
    codes_barre_entre_stock.append(codes_texte_entre_stock[i][:-1])
#sortie stock :

codes_texte_sortie_stock=sortie_stock.readlines()
codes_barre_sortie_stock=[]
for i in range(len(codes_texte_sortie_stock)-1):
    codes_barre_sortie_stock.append(codes_texte_sortie_stock[i][:-1])

#Entrée Atelier 1 :

codes_texte1=entre1.readlines()
codes_barre_entre1=[]
for i in range(len(codes_texte1)-1):
    codes_barre_entre1.append(codes_texte1[i][:-1])
#sortie atelier 1 :

codes_texte_sortie1=sortie1.readlines()
codes_barre_sortie1=[]
for i in range(len(codes_texte_sortie1)):
    codes_barre_sortie1.append(codes_texte_sortie1[i][:-1])
#Entrée atelier 2 :
codes_texte2=entre2.readlines()
codes_barre_entre2=[]
for i in range(len(codes_texte2)-1):
    codes_barre_entre2.append(codes_texte2[i][:-1])
#sortie atelier 2:

codes_texte_sortie2=sortie2.readlines()
codes_barre_sortie2=[]
for i in range(len(codes_texte_sortie2)):
    codes_barre_sortie2.append(codes_texte_sortie2[i][:-1])
#Ouvrir la base de données :
doc=xlrd.open_workbook("base de données.xlsx")
feuille_1 = doc.sheet_by_index(0)
rows = feuille_1.nrows
codes_base=[]
for i in range(1,rows):
    cellule = feuille_1.cell_value(rowx=i, colx=0)
    codes_base.append(cellule)
#fonction qui prend une liste et retourne une liste clean :
def nombre_rep(L):
    X=[]
    for l in L:
        X.append(l)
    for l in X:
        n=X.count(l)
        if n>1:
            for i in range(n-1):
                X.remove(l)
    
   
    return X
clients=[]
for i in range(1,rows):
    cellule = feuille_1.cell_value(rowx=i, colx=1)
    clients.append(cellule)
client_base=nombre_rep(clients)
#print('clients = ',client_base)

typs=[]
for i in range(1,rows):
    cellule = feuille_1.cell_value(rowx=i, colx=2)
    typs.append(cellule)
type_base=nombre_rep(typs)
#print("types = ",type_base)
print([1,1,1,0,2,3,1,0,0,3,4,0,3])
print(nombre_rep([1,1,1,0,2,3,1,0,0,3,4,0,3]))
#print("codes barre = ",codes_barre)
#print("codes base = ", codes_base)
#print("code barre clean = ",codes_barre_clean)

#Créer la liste des bidons entrées au stock :
codes_barre_clean_entre_stock=nombre_rep(codes_barre_entre_stock)
list_bidon_entre_stock=[]
for code in codes_barre_clean_entre_stock :
    if code in codes_base:       
        client_bidon = feuille_1.cell_value(rowx=codes_base.index(code)+1, colx=1)
        type_bidon = feuille_1.cell_value(rowx=codes_base.index(code)+1, colx=2)
        comptage=codes_barre_entre_stock.count(code)
        bidon={"code":code, "client":client_bidon, "type":type_bidon,"comptage_entre_stock":comptage}
        list_bidon_entre_stock.append(bidon) 
print("liste des bidons à l'entre du stock = ",list_bidon_entre_stock)
#Créer la liste des bidons à la sortie du stock :
codes_barre_clean_sortie_stock=nombre_rep(codes_barre_sortie_stock)

list_bidon_sortie_stock=[]
for code in codes_barre_clean_sortie_stock :
    if code in codes_base:       
        client_bidon = feuille_1.cell_value(rowx=codes_base.index(code)+1, colx=1)
        type_bidon = feuille_1.cell_value(rowx=codes_base.index(code)+1, colx=2)
        comptage=codes_barre_sortie_stock.count(code)
        bidon={"code":code, "client":client_bidon, "type":type_bidon,"comptage_sortie_stock":comptage}
        list_bidon_sortie_stock.append(bidon)
print("liste des bidons à la sortie du stock=",list_bidon_sortie_stock)
#Créer une liste bidon du reste de stock :
list_bidon_stock=[]
for bidon_entree in list_bidon_entre_stock:
    code=bidon_entree["code"]
    comptage_sortie=0
    for bidon_sortie in list_bidon_sortie_stock:
        if bidon_sortie["code"]==code :
            comptage_sortie=bidon_sortie["comptage_sortie_stock"]
            break
    reste_stock=bidon_entree["comptage_entre_stock"]-comptage_sortie
    bidon_stock={"code":code,"client":bidon_entree["client"],"type":bidon_entree["type"],"comptage_entre_stock":bidon_entree["comptage_entre_stock"],"comptage_sortie_stock":comptage_sortie,"reste":reste_stock}
    list_bidon_stock.append(bidon_stock)
print("liste bidon stock =",list_bidon_stock)
#Créer la liste des bidons entrées à l'atelier 1 : 
codes_barre_clean_entre1=nombre_rep(codes_barre_entre1)
list_bidon_entre1=[]
for code in codes_barre_clean_entre1 :
    if code in codes_base:       
        client_bidon = feuille_1.cell_value(rowx=codes_base.index(code)+1, colx=1)
        type_bidon = feuille_1.cell_value(rowx=codes_base.index(code)+1, colx=2)
        comptage=codes_barre_entre1.count(code)
        bidon={"code":code, "client":client_bidon, "type":type_bidon,"comptage_entre1":comptage}
        list_bidon_entre1.append(bidon) 
print("liste des bidons entree à l'atelier 1 = ", list_bidon_entre1)
#Créer la liste des bidons à la sortie de l'atelier 1 :
codes_barre_clean_sortie1=nombre_rep(codes_barre_sortie1)
list_bidon_sortie1=[]
for code in codes_barre_clean_sortie1 :
    if code in codes_base:       
        client_bidon = feuille_1.cell_value(rowx=codes_base.index(code)+1, colx=1)
        type_bidon = feuille_1.cell_value(rowx=codes_base.index(code)+1, colx=2)
        comptage=codes_barre_sortie1.count(code)
        bidon={"code":code, "client":client_bidon, "type":type_bidon,"comptage_sortie1":comptage}
        list_bidon_sortie1.append(bidon) 
print("list des bidons à la sortie de l'atelier 1 = ",list_bidon_sortie1)
#Créer liste des bidons qui reste dans l'atelier 1 :
list_bidon=[]
for bidon_entree in list_bidon_entre1:
    code=bidon_entree["code"]
    comptage_sortie=0
    for bidon_sortie in list_bidon_sortie1:
        if bidon_sortie["code"]==code :
            comptage_sortie=bidon_sortie["comptage_sortie1"]
            break
    for bidon_stock in list_bidon_stock:
        if bidon_stock["code"]==code:
            comptage_stock=bidon_stock["reste"]
            break
    comptage=bidon_entree["comptage_entre1"]-comptage_sortie
    bidon={"code":code,"client":bidon_entree["client"],"type":bidon_entree["type"],"comptage_entre1":bidon_entree["comptage_entre1"],"comptage_sortie1":comptage_sortie,"comptage":comptage,"comptage_stock":comptage_stock}
    list_bidon.append(bidon)
print("list bidon  =",list_bidon)   
#Créer la liste des bidons entrées à l'atelier 2 : 
codes_barre_clean_entre2=nombre_rep(codes_barre_entre2)
list_bidon_entre2=[]
for code in codes_barre_clean_entre2 :
    if code in codes_base:       
        client_bidon = feuille_1.cell_value(rowx=codes_base.index(code)+1, colx=1)
        type_bidon = feuille_1.cell_value(rowx=codes_base.index(code)+1, colx=2)
        comptage=codes_barre_entre2.count(code)
        bidon={"code":code, "client":client_bidon, "type":type_bidon,"comptage_entre2":comptage}
        list_bidon_entre2.append(bidon) 
print("liste des bidons entree à l'atelier 2 = ", list_bidon_entre2)
#Créer la liste des bidons à la sortie de l'atelier 2 :
codes_barre_clean_sortie2=nombre_rep(codes_barre_sortie2)
list_bidon_sortie2=[]
for code in codes_barre_clean_sortie2 :
    if code in codes_base:       
        client_bidon = feuille_1.cell_value(rowx=codes_base.index(code)+1, colx=1)
        type_bidon = feuille_1.cell_value(rowx=codes_base.index(code)+1, colx=2)
        comptage=codes_barre_sortie2.count(code)
        bidon={"code":code, "client":client_bidon, "type":type_bidon,"comptage_sortie2":comptage}
        list_bidon_sortie2.append(bidon) 
print("list des bidons à la sortie de l'atelier 2 = ",list_bidon_sortie2)
#Créer liste des bidons qui reste dans l'atelier 2 :
list_bidon2=[]
for bidon_entree in list_bidon_entre2:
    code=bidon_entree["code"]
    comptage_sortie=0
    for bidon_sortie in list_bidon_sortie2:
        if bidon_sortie["code"]==code :
            comptage_sortie=bidon_sortie["comptage_sortie2"]
            break
    for bidon_stock in list_bidon_stock:
        if bidon_stock["code"]==code:
            comptage_stock=bidon_stock["reste"]
            break
    comptage=bidon_entree["comptage_entre2"]-comptage_sortie
    bidon={"code":code,"client":bidon_entree["client"],"type":bidon_entree["type"],"comptage_entre2":bidon_entree["comptage_entre2"],"comptage_sortie2":comptage_sortie,"comptage":comptage,"comptage_stock":comptage_stock}
    list_bidon2.append(bidon)
print("list bidon2 =",list_bidon2)



"""fichier=xlwt.Workbook()
sheet=fichier.add_sheet("Comptage")
sheet.write(0,0,"Client")
sheet.write(0,1,"Type")
sheet.write(0,2,"Comptage")
for i in range(len(list_bidon)):
    Client=list_bidon[i]["client"]
    Type=list_bidon[i]["type"]
    Comptage=list_bidon[i]["comptage"]
    sheet.write(i+1,0,Client)
    sheet.write(i+1,1,Type)
    sheet.write(i+1,2,Comptage)
fichier.save("compt2.xls")"""
#La fonction espace : 
def espace(phrase):
    for l in phrase :
        if l==" ":
            i=phrase.index(l)
            break
    return phrase[i:]
#La commande de button Atelier1 :
def Atelier1():
    #La fonction du boutton recherche : 
    def Recherche():
        #La fonction du button rechercher : 
        #global entryClient, entryType, entryComptage, entryComptageClient, entryComptageType, entryDate, entryHeure 
        def action():
            client=entryClient.get()
            typ=entryType.get()
            if client not in client_base and typ in type_base:
                messagebox.showerror("Ereur client","Veuillez entrez un client existant")
            if typ not in type_base and client in client_base:
                messagebox.showerror("Ereur type","Veuillez entrez un type existant")
            if typ not in type_base and client not in client_base:
                messagebox.showerror("Ereur client et type","Veuillez entrez un client et un type existant")
            k=False
            for bidon in list_bidon:
                if bidon["client"]==client and bidon["type"]==typ:
                    bidon_corr=bidon
                    comptage=bidon_corr["comptage"]
                    k=True
                    break
            if k==False:
                comptage=0
            comptage_client=0
            for bidon in list_bidon:
                if bidon["client"]==client:
                    comptage_client+=bidon["comptage"]
            comptage_type=0
            for bidon in list_bidon:
                if bidon["type"]==typ:
                    comptage_type+=bidon["comptage"]
            

            Date=datetime.date.today()
            Heure=espace(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) 
            entryComptage.delete(0, END)
            entryComptageClient.delete(0,END)
            entryComptageType.delete(0,END)
            entryDate.delete(0, END)
            entryHeure.delete(0, END)
            entryComptage.insert(0, comptage)
            entryComptageClient.insert(0, comptage_client)
            entryComptageType.insert(0, comptage_type)
            entryDate.insert(0, Date)
            entryHeure.insert(0, Heure)
        #Fenetre du button recherche dans l'atelier 1 :
        top1=Tk()
        top1.title("Recherche dans l'atelier 1")
        top1.geometry("1080x720")
        top1.iconbitmap('logo.ico')
        top1.configure(background="#41B77F")
        #Client
        lablClient=Label(top1, text='Client : ')
        lablClient.place(x=400, y=100)
        entryClient=Entry(top1)
        entryClient.place(x=600, y=100)
        #Type
        lablType=Label(top1, text='Type : ')
        lablType.place(x=400,y=150)
        entryType=Entry(top1)
        entryType.place(x=600,y=150)
        #Comptage
        lablComptage=Label(top1, text='Comptage  :')
        lablComptage.place(x=400,y=200)
        entryComptage=Entry(top1,fg="red")
        entryComptage.place(x=600,y=200)
        #Total comtage par client
        lablComptageClient=Label(top1, text='Comptage par client :')
        lablComptageClient.place(x=400,y=250)
        entryComptageClient=Entry(top1,fg="red")
        entryComptageClient.place(x=600,y=250)
        #Total comptage par type
        lablComptageType=Label(top1, text='Comptage par type :')
        lablComptageType.place(x=400,y=300)
        entryComptageType=Entry(top1,fg="red")
        entryComptageType.place(x=600,y=300)
        #Date 
        lablDate=Label(top1, text='Date  :')
        lablDate.place(x=400,y=350)
        entryDate=Entry(top1,fg="red")
        entryDate.place(x=600,y=350)
        #Heure
        lablHeure=Label(top1, text='Heure  :')
        lablHeure.place(x=400,y=400)
        entryHeure=Entry(top1,fg="red")
        entryHeure.place(x=600,y=400)
        #Button recherche
        rechercher=Button(top1, text="Rechercher", font=("Courrier",20), bg="blue", fg='white', command=action)
        rechercher.place(x=600,y=450)
        #Button quitter : 
        quitter=Button(top1, text="Quitter",font=('Courrier',20),bg="red",fg="white",command=top1.quit)
        quitter.place(x=350,y=450)
    def stock():
        #fonction du client A : 
        def A():
            topA=Tk()
            topA.title("Déchets du client A dans l'atelier 1")
            topA.geometry("1350x1350")
            topA.iconbitmap('logo.ico')
            topA.configure(background="#41B77F")
            #Time :
            Label(topA,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topA,text="l'état du stock du client A dans l'atelier 1",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topA,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topA,text="A",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topA,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientA=0
            for bidon in list_bidon:
                if bidon["client"]=='A':
                    comptage_clientA+=bidon["comptage"]
            Label(topA,text=comptage_clientA,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topA,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon:
                if bidon["client"]=="A" and bidon["type"]=="solvant":
                   comptage_solvantA=bidon["comptage"]
                   k=True
                   break
            if k==False:
                comptage_solvantA=0
            Label(topA,text=comptage_solvantA,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topA,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon:
                if bidon["client"]=="A" and bidon["type"]=="liquide":
                   comptage_liquideA=bidon["comptage"]
                   l=True
                   break
            if l==False :
                comptage_liquideA=0
            Label(topA,text=comptage_liquideA,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topA,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon:
                if bidon["client"]=="A" and bidon["type"]=="solide":
                   comptage_solideA=bidon["comptage"]
                   s=True
                   break
            if s==False :
                comptage_solideA=0 
            Label(topA,text=comptage_solideA,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #fonction du client B : 
        def B():
            topB=Tk()
            topB.title("Déchets du client B dans l'atelier 1")
            topB.geometry("1350x1350")
            topB.iconbitmap('logo.ico')
            topB.configure(background="#41B77F")
            #Time :
            Label(topB,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topB,text="l'état du stock du client B dans l'atelier 1",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topB,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topB,text="B",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topB,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientB=0
            for bidon in list_bidon:
                if bidon["client"]=='B':
                    comptage_clientB+=bidon["comptage"]
            Label(topB,text=comptage_clientB,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topB,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon:
                if bidon["client"]=="B" and bidon["type"]=="solvant":
                   comptage_solvantB=bidon["comptage"]
                   k=True
                   break
            if k==False:
                comptage_solvantB=0
            Label(topB,text=comptage_solvantB,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topB,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon:
                if bidon["client"]=="B" and bidon["type"]=="liquide":
                   comptage_liquideB=bidon["comptage"]
                   l=True
                   break
            if l==False :
                comptage_liquideB=0
            Label(topB,text=comptage_liquideB,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topB,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon:
                if bidon["client"]=="B" and bidon["type"]=="solide":
                   comptage_solideB=bidon["comptage"]
                   s=True
                   break
            if s==False :
                comptage_solideB=0 
            Label(topB,text=comptage_solideB,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #fonction du client C : 
        def C():
            topC=Tk()
            topC.title("Déchets  du client C dans l'atelier 1")
            topC.geometry("1350x1350")
            topC.iconbitmap('logo.ico')
            topC.configure(background="#41B77F")
            #Time :
            Label(topC,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topC,text="l'état du stock du client C dans l'atelier 1",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topC,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topC,text="C",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topC,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientC=0
            for bidon in list_bidon:
                if bidon["client"]=='C':
                    comptage_clientC+=bidon["comptage"]
            Label(topC,text=comptage_clientC,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topC,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon:
                if bidon["client"]=="C" and bidon["type"]=="solvant":
                   comptage_solvantC=bidon["comptage"]
                   k=True
                   break
            if k==False:
                comptage_solvantC=0
            Label(topC,text=comptage_solvantC,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topC,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon:
                if bidon["client"]=="C" and bidon["type"]=="liquide":
                   comptage_liquideC=bidon["comptage"]
                   l=True
                   break
            if l==False :
                comptage_liquideC=0
            Label(topC,text=comptage_liquideC,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topC,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon:
                if bidon["client"]=="C" and bidon["type"]=="solide":
                   comptage_solideC=bidon["comptage"]
                   s=True
                   break
            if s==False :
                comptage_solideC=0 
            Label(topC,text=comptage_solideC,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #fonction du client D : 
        def D():
            topD=Tk()
            topD.title("Déchets du client D dans l'atelier 1")
            topD.geometry("1350x1350")
            topD.iconbitmap('logo.ico')
            topD.configure(background="#41B77F")
            #Time :
            Label(topD,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topD,text="l'état du stock du client D dans l'atelier 1",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topD,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topD,text="D",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topD,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientD=0
            for bidon in list_bidon:
                if bidon["client"]=='D':
                    comptage_clientD+=bidon["comptage"]
            Label(topD,text=comptage_clientD,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topD,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon:
                if bidon["client"]=="D" and bidon["type"]=="solvant":
                   comptage_solvantD=bidon["comptage"]
                   k=True
                   break
            if k==False:
                comptage_solvantD=0
            Label(topD,text=comptage_solvantD,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topD,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon:
                if bidon["client"]=="D" and bidon["type"]=="liquide":
                   comptage_liquideD=bidon["comptage"]
                   l=True
                   break
            if l==False :
                comptage_liquideD=0
            Label(topD,text=comptage_liquideD,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topD,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon:
                if bidon["client"]=="D" and bidon["type"]=="solide":
                   comptage_solideD=bidon["comptage"]
                   s=True
                   break
            if s==False :
                comptage_solideD=0 
            Label(topD,text=comptage_solideD,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #fonction du client E : 
        def E():
            topE=Tk()
            topE.title("Déchets du client E dans l'atelier 1")
            topE.geometry("1350x1350")
            topE.iconbitmap('logo.ico')
            topE.configure(background="#41B77F")
            #Time :
            Label(topE,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topE,text="l'état du stock du client E dans l'atelier 1",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topE,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topE,text="E",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topE,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientE=0
            for bidon in list_bidon:
                if bidon["client"]=='E':
                    comptage_clientE+=bidon["comptage"]
            Label(topE,text=comptage_clientE,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topE,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon:
                if bidon["client"]=="E" and bidon["type"]=="solvant":
                   comptage_solvantE=bidon["comptage"]
                   k=True
                   break
            if k==False:
                comptage_solvantE=0
            Label(topE,text=comptage_solvantE,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topE,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon:
                if bidon["client"]=="E" and bidon["type"]=="liquide":
                   comptage_liquideE=bidon["comptage"]
                   l=True
                   break
            if l==False :
                comptage_liquideE=0
            Label(topE,text=comptage_liquideE,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topE,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon:
                if bidon["client"]=="E" and bidon["type"]=="solide":
                   comptage_solideE=bidon["comptage"]
                   s=True
                   break
            if s==False :
                comptage_solideE=0 
            Label(topE,text=comptage_solideE,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #fonction du client F : 
        def F():
            topF=Tk()
            topF.title("Déchets du client F dans l'atelier 1")
            topF.geometry("1350x1350")
            topF.iconbitmap('logo.ico')
            topF.configure(background="#41B77F")
            #Time :
            Label(topF,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topF,text="l'état du stock du client F dans l'atelier 1",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topF,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topF,text="F",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topF,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientF=0
            for bidon in list_bidon:
                if bidon["client"]=='F':
                    comptage_clientF+=bidon["comptage"]
            Label(topF,text=comptage_clientF,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topF,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon:
                if bidon["client"]=="F" and bidon["type"]=="solvant":
                   comptage_solvantF=bidon["comptage"]
                   k=True
                   break
            if k==False:
                comptage_solvantF=0
            Label(topF,text=comptage_solvantF,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topF,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon:
                if bidon["client"]=="F" and bidon["type"]=="liquide":
                   comptage_liquideF=bidon["comptage"]
                   l=True
                   break
            if l==False :
                comptage_liquideF=0
            Label(topF,text=comptage_liquideF,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topF,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon:
                if bidon["client"]=="F" and bidon["type"]=="solide":
                   comptage_solideF=bidon["comptage"]
                   s=True
                   break
            if s==False :
                comptage_solideF=0 
            Label(topF,text=comptage_solideF,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #fonction du client G : 
        def G():
            topG=Tk()
            topG.title("Déchets du client G dans l'atelier 2")
            topG.geometry("1350x1350")
            topG.iconbitmap('logo.ico')
            topG.configure(background="#41B77F")
            #Time :
            Label(topG,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topG,text="l'état du stock du client G dans l'atelier 1",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topG,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topG,text="G",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topG,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientG=0
            for bidon in list_bidon:
                if bidon["client"]=='G':
                    comptage_clientG+=bidon["comptage"]
            Label(topG,text=comptage_clientG,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topG,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon:
                if bidon["client"]=="G" and bidon["type"]=="solvant":
                   comptage_solvantG=bidon["comptage"]
                   k=True
                   break
            if k==False:
                comptage_solvantG=0
            Label(topG,text=comptage_solvantG,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topG,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon:
                if bidon["client"]=="G" and bidon["type"]=="liquide":
                   comptage_liquideG=bidon["comptage"]
                   l=True
                   break
            if l==False :
                comptage_liquideG=0
            Label(topG,text=comptage_liquideG,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topG,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon:
                if bidon["client"]=="G" and bidon["type"]=="solide":
                   comptage_solideG=bidon["comptage"]
                   s=True
                   break
            if s==False :
                comptage_solideG=0 
            Label(topG,text=comptage_solideG,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #Fentere de stock : 
        top2=Tk()
        top2.title("stock de l'atelier 1")
        top2.geometry("1080x720")
        top2.iconbitmap('logo.ico')
        top2.configure(background="#41B77F")
        #Création des textes :
        texte_stock1=Label(top2,text="Gestion des clients dans le stock",font=("Courrier",40),bg="#41B77F",fg="white")
        texte_stock1.place(x=150,y=50)
        texte_stock2=Label(top2,text="   De l'atelier 1   ",font=("Courrier",40),bg="#41B77F",fg="white")
        texte_stock2.place(x=350,y=150)
        #Création des bouttons :
        #A
        Button(top2,text="A",font=('Courrier',25),bg="black",fg="white",command=A).place(x=50,y=300)
        #B
        Button(top2,text="B",font=('Courrier',25),bg="black",fg="white",command=B).place(x=300,y=300)
        #C
        Button(top2,text="C",font=('Courrier',25),bg="black",fg="white",command=C).place(x=550,y=300)
        #D
        Button(top2,text="D",font=('Courrier',25),bg="black",fg="white",command=D).place(x=800,y=300)
        #E
        Button(top2,text="E",font=('Courrier',25),bg="black",fg="white",command=E).place(x=50,y=500)
        #F
        Button(top2,text="F",font=('Courrier',25),bg="black",fg="white",command=F).place(x=300,y=500)
        #G
        Button(top2,text="G",font=('Courrier',25),bg="black",fg="white",command=G).place(x=550,y=500)
        
    top=Tk()
    top.title("Atelier 1")
    top.geometry("1080x720")
    top.iconbitmap('logo.ico')
    top.configure(background="#41B77F")
    #Ajouter texte :
    label_title=Label(top, text="Gestion de  l'atelier 1 ", font=("Courrier",60),bg="#41B77F", fg='white')
    label_title.pack(expand=YES)
    #Recherche Button : 
    Recherche=Button(top, text="Recherche",font=("Courrier",20),bg="blue", fg='white', command=Recherche)
    Recherche.place(x=300, y=0)
    #Button stock :
    stock=Button(top, text="Stock",font=("Courrier",20),bg="blue", fg='white', command=stock)
    stock.place(x=500,y=0)
    #Button quitter :
    quitter=Button(top, text="Quitter",font=("Courrier",20),bg="red", fg='white', command=top.quit)
    quitter.place(x=650,y=0)


#La commande de button Atelier2 :
def Atelier2():
    #La fonction du boutton recherche : 
    def Recherche():
        #La fonction du button rechercher : 
        #global entryClient, entryType, entryComptage, entryComptageClient, entryComptageType, entryDate, entryHeure 
        def action():
            client=entryClient.get()
            typ=entryType.get()
            if client not in client_base and typ in type_base:
                messagebox.showerror("Ereur client","Veuillez entrez un client existant")
            if typ not in type_base and client in client_base:
                messagebox.showerror("Ereur type","Veuillez entrez un type existant")
            if typ not in type_base and client not in client_base:
                messagebox.showerror("Ereur client et type","Veuillez entrez un client et un type existant")
            k=False
            for bidon in list_bidon2:
                if bidon["client"]==client and bidon["type"]==typ:
                    bidon_corr=bidon
                    comptage=bidon_corr["comptage"]
                    k=True
                    break
            if k==False:
                comptage=0
            comptage_client=0
            for bidon in list_bidon2:
                if bidon["client"]==client:
                    comptage_client+=bidon["comptage"]
            comptage_type=0
            for bidon in list_bidon2:
                if bidon["type"]==typ:
                    comptage_type+=bidon["comptage"]
            

            Date=datetime.date.today()
            Heure=espace(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) 
            entryComptage.delete(0, END)
            entryComptageClient.delete(0,END)
            entryComptageType.delete(0,END)
            entryDate.delete(0, END)
            entryHeure.delete(0, END)
            entryComptage.insert(0, comptage)
            entryComptageClient.insert(0, comptage_client)
            entryComptageType.insert(0, comptage_type)
            entryDate.insert(0, Date)
            entryHeure.insert(0, Heure)
        #Fenetre du button recherche dans l'atelier 1 :
        top1=Tk()
        top1.title("Recherche dans l'atelier 2")
        top1.geometry("1080x720")
        top1.iconbitmap('logo.ico')
        top1.configure(background="#41B77F")
        #Client
        lablClient=Label(top1, text='Client : ')
        lablClient.place(x=400, y=100)
        entryClient=Entry(top1)
        entryClient.place(x=600, y=100)
        #Type
        lablType=Label(top1, text='Type : ')
        lablType.place(x=400,y=150)
        entryType=Entry(top1)
        entryType.place(x=600,y=150)
        #Comptage
        lablComptage=Label(top1, text='Comptage  :')
        lablComptage.place(x=400,y=200)
        entryComptage=Entry(top1,fg="red")
        entryComptage.place(x=600,y=200)
        #Total comtage par client
        lablComptageClient=Label(top1, text='Comptage par client :')
        lablComptageClient.place(x=400,y=250)
        entryComptageClient=Entry(top1,fg="red")
        entryComptageClient.place(x=600,y=250)
        #Total comptage par type
        lablComptageType=Label(top1, text='Comptage par type :')
        lablComptageType.place(x=400,y=300)
        entryComptageType=Entry(top1,fg="red")
        entryComptageType.place(x=600,y=300)
        #Date 
        lablDate=Label(top1, text='Date  :')
        lablDate.place(x=400,y=350)
        entryDate=Entry(top1,fg="red")
        entryDate.place(x=600,y=350)
        #Heure
        lablHeure=Label(top1, text='Heure  :')
        lablHeure.place(x=400,y=400)
        entryHeure=Entry(top1,fg="red")
        entryHeure.place(x=600,y=400)
        #Button recherche
        rechercher=Button(top1, text="Rechercher", font=("Courrier",20), bg="blue", fg='white', command=action)
        rechercher.place(x=600,y=450)
        #Button quitter : 
        quitter=Button(top1, text="Quitter",font=('Courrier',20),bg="red",fg="white",command=top1.quit)
        quitter.place(x=350,y=450)
    def stock():
        #fonction du client A : 
        def A():
            topA=Tk()
            topA.title("déchets du client A dans l'atelier 2")
            topA.geometry("1350x1350")
            topA.iconbitmap('logo.ico')
            topA.configure(background="#41B77F")
            #Time :
            Label(topA,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topA,text="l'état du stock du client A dans l'atelier 2",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topA,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topA,text="A",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topA,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientA=0
            for bidon in list_bidon2:
                if bidon["client"]=='A':
                    comptage_clientA+=bidon["comptage"]
            Label(topA,text=comptage_clientA,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topA,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon2:
                if bidon["client"]=="A" and bidon["type"]=="solvant":
                   comptage_solvantA=bidon["comptage"]
                   k=True
                   break
            if k==False:
                comptage_solvantA=0
            Label(topA,text=comptage_solvantA,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topA,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon2:
                if bidon["client"]=="A" and bidon["type"]=="liquide":
                   comptage_liquideA=bidon["comptage"]
                   l=True
                   break
            if l==False :
                comptage_liquideA=0
            Label(topA,text=comptage_liquideA,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topA,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon2:
                if bidon["client"]=="A" and bidon["type"]=="solide":
                   comptage_solideA=bidon["comptage"]
                   s=True
                   break
            if s==False :
                comptage_solideA=0 
            Label(topA,text=comptage_solideA,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #fonction du client B : 
        def B():
            topB=Tk()
            topB.title("Déchets du client B dans l'atelier 2 ")
            topB.geometry("1350x1350")
            topB.iconbitmap('logo.ico')
            topB.configure(background="#41B77F")
            #Time :
            Label(topB,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topB,text="l'état du stock du client B dans l'atelier 2",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topB,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topB,text="B",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topB,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientB=0
            for bidon in list_bidon2:
                if bidon["client"]=='B':
                    comptage_clientB+=bidon["comptage"]
            Label(topB,text=comptage_clientB,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topB,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon2:
                if bidon["client"]=="B" and bidon["type"]=="solvant":
                   comptage_solvantB=bidon["comptage"]
                   k=True
                   break
            if k==False:
                comptage_solvantB=0
            Label(topB,text=comptage_solvantB,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topB,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon2:
                if bidon["client"]=="B" and bidon["type"]=="liquide":
                   comptage_liquideB=bidon["comptage"]
                   l=True
                   break
            if l==False :
                comptage_liquideB=0
            Label(topB,text=comptage_liquideB,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topB,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon2:
                if bidon["client"]=="B" and bidon["type"]=="solide":
                   comptage_solideB=bidon["comptage"]
                   s=True
                   break
            if s==False :
                comptage_solideB=0 
            Label(topB,text=comptage_solideB,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #fonction du client C : 
        def C():
            topC=Tk()
            topC.title("Déchets du client C dans l'atelier 2")
            topC.geometry("1350x1350")
            topC.iconbitmap('logo.ico')
            topC.configure(background="#41B77F")
            #Time :
            Label(topC,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topC,text="l'état du stock du client C dans l'atelier 2",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topC,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topC,text="C",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topC,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientC=0
            for bidon in list_bidon2:
                if bidon["client"]=='C':
                    comptage_clientC+=bidon["comptage"]
            Label(topC,text=comptage_clientC,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topC,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon2:
                if bidon["client"]=="C" and bidon["type"]=="solvant":
                   comptage_solvantC=bidon["comptage"]
                   k=True
                   break
            if k==False:
                comptage_solvantC=0
            Label(topC,text=comptage_solvantC,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topC,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon2:
                if bidon["client"]=="C" and bidon["type"]=="liquide":
                   comptage_liquideC=bidon["comptage"]
                   l=True
                   break
            if l==False :
                comptage_liquideC=0
            Label(topC,text=comptage_liquideC,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topC,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon2:
                if bidon["client"]=="C" and bidon["type"]=="solide":
                   comptage_solideC=bidon["comptage"]
                   s=True
                   break
            if s==False :
                comptage_solideC=0 
            Label(topC,text=comptage_solideC,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #fonction du client D : 
        def D():
            topD=Tk()
            topD.title("Déchets du client D dans l'atelier 2")
            topD.geometry("1350x1350")
            topD.iconbitmap('logo.ico')
            topD.configure(background="#41B77F")
            #Time :
            Label(topD,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topD,text="l'état du stock du client D dans l'atelier 2",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topD,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topD,text="D",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topD,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientD=0
            for bidon in list_bidon2:
                if bidon["client"]=='D':
                    comptage_clientD+=bidon["comptage"]
            Label(topD,text=comptage_clientD,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topD,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon2:
                if bidon["client"]=="D" and bidon["type"]=="solvant":
                   comptage_solvantD=bidon["comptage"]
                   k=True
                   break
            if k==False:
                comptage_solvantD=0
            Label(topD,text=comptage_solvantD,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topD,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon2:
                if bidon["client"]=="D" and bidon["type"]=="liquide":
                   comptage_liquideD=bidon["comptage"]
                   l=True
                   break
            if l==False :
                comptage_liquideD=0
            Label(topD,text=comptage_liquideD,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topD,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon2:
                if bidon["client"]=="D" and bidon["type"]=="solide":
                   comptage_solideD=bidon["comptage"]
                   s=True
                   break
            if s==False :
                comptage_solideD=0 
            Label(topD,text=comptage_solideD,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #fonction du client E : 
        def E():
            topE=Tk()
            topE.title("Déchets du client E dans l'atelier 2")
            topE.geometry("1350x1350")
            topE.iconbitmap('logo.ico')
            topE.configure(background="#41B77F")
            #Time :
            Label(topE,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topE,text="l'état du stock du client E dans l'atelier 2",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topE,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topE,text="E",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topE,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientE=0
            for bidon in list_bidon2:
                if bidon["client"]=='E':
                    comptage_clientE+=bidon["comptage"]
            Label(topE,text=comptage_clientE,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topE,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon2:
                if bidon["client"]=="E" and bidon["type"]=="solvant":
                   comptage_solvantE=bidon["comptage"]
                   k=True
                   break
            if k==False:
                comptage_solvantE=0
            Label(topE,text=comptage_solvantE,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topE,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon2:
                if bidon["client"]=="E" and bidon["type"]=="liquide":
                   comptage_liquideE=bidon["comptage"]
                   l=True
                   break
            if l==False :
                comptage_liquideE=0
            Label(topE,text=comptage_liquideE,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topE,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon2:
                if bidon["client"]=="E" and bidon["type"]=="solide":
                   comptage_solideE=bidon["comptage"]
                   s=True
                   break
            if s==False :
                comptage_solideE=0 
            Label(topE,text=comptage_solideE,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #fonction du client F : 
        def F():
            topF=Tk()
            topF.title("Déchets du client F dans l'atelier 2")
            topF.geometry("1350x1350")
            topF.iconbitmap('logo.ico')
            topF.configure(background="#41B77F")
            #Time :
            Label(topF,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topF,text="l'état du stock du client F dans l'atelier 2",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topF,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topF,text="F",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topF,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientF=0
            for bidon in list_bidon2:
                if bidon["client"]=='F':
                    comptage_clientF+=bidon["comptage"]
            Label(topF,text=comptage_clientF,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topF,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon2:
                if bidon["client"]=="F" and bidon["type"]=="solvant":
                   comptage_solvantF=bidon["comptage"]
                   k=True
                   break
            if k==False:
                comptage_solvantF=0
            Label(topF,text=comptage_solvantF,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topF,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon2:
                if bidon["client"]=="F" and bidon["type"]=="liquide":
                   comptage_liquideF=bidon["comptage"]
                   l=True
                   break
            if l==False :
                comptage_liquideF=0
            Label(topF,text=comptage_liquideF,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topF,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon2:
                if bidon["client"]=="F" and bidon["type"]=="solide":
                   comptage_solideF=bidon["comptage"]
                   s=True
                   break
            if s==False :
                comptage_solideF=0 
            Label(topF,text=comptage_solideF,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #fonction du client G : 
        def G():
            topG=Tk()
            topG.title("Déchets du client G dans l'atelier 2")
            topG.geometry("1350x1350")
            topG.iconbitmap('logo.ico')
            topG.configure(background="#41B77F")
            #Time :
            Label(topG,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topG,text="l'état du stock du client G dans l'atelier 2",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topG,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topG,text="G",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topG,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientG=0
            for bidon in list_bidon2:
                if bidon["client"]=='G':
                    comptage_clientG+=bidon["comptage"]
            Label(topG,text=comptage_clientG,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topG,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon2:
                if bidon["client"]=="G" and bidon["type"]=="solvant":
                   comptage_solvantG=bidon["comptage"]
                   k=True
                   break
            if k==False:
                comptage_solvantG=0
            Label(topG,text=comptage_solvantG,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topG,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon2:
                if bidon["client"]=="G" and bidon["type"]=="liquide":
                   comptage_liquideG=bidon["comptage"]
                   l=True
                   break
            if l==False :
                comptage_liquideG=0
            Label(topG,text=comptage_liquideG,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topG,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon2:
                if bidon["client"]=="G" and bidon["type"]=="solide":
                   comptage_solideG=bidon["comptage"]
                   s=True
                   break
            if s==False :
                comptage_solideG=0 
            Label(topG,text=comptage_solideG,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #Fentere de stock : 
        top2=Tk()
        top2.title("stock de l'atelier 2")
        top2.geometry("1080x720")
        top2.iconbitmap('logo.ico')
        top2.configure(background="#41B77F")
        #Création des textes :
        texte_stock1=Label(top2,text="Gestion des clients dans le stock",font=("Courrier",40),bg="#41B77F",fg="white")
        texte_stock1.place(x=150,y=50)
        texte_stock2=Label(top2,text="   De l'atelier 2   ",font=("Courrier",40),bg="#41B77F",fg="white")
        texte_stock2.place(x=350,y=150)
        #Création des bouttons :
        #A
        Button(top2,text="A",font=('Courrier',25),bg="black",fg="white",command=A).place(x=50,y=300)
        #B
        Button(top2,text="B",font=('Courrier',25),bg="black",fg="white",command=B).place(x=300,y=300)
        #C
        Button(top2,text="C",font=('Courrier',25),bg="black",fg="white",command=C).place(x=550,y=300)
        #D
        Button(top2,text="D",font=('Courrier',25),bg="black",fg="white",command=D).place(x=800,y=300)
        #E
        Button(top2,text="E",font=('Courrier',25),bg="black",fg="white",command=E).place(x=50,y=500)
        #F
        Button(top2,text="F",font=('Courrier',25),bg="black",fg="white",command=F).place(x=300,y=500)
        #G
        Button(top2,text="G",font=('Courrier',25),bg="black",fg="white",command=G).place(x=550,y=500)
        
    top=Tk()
    top.title("Atelier 2")
    top.geometry("1080x720")
    top.iconbitmap('logo.ico')
    top.configure(background="#41B77F")
    #Ajouter texte :
    label_title=Label(top, text="Gestion de  l'atelier 2 ", font=("Courrier",60),bg="#41B77F", fg='white')
    label_title.pack(expand=YES)
    #Recherche Button : 
    Recherche=Button(top, text="Recherche",font=("Courrier",20),bg="blue", fg='white', command=Recherche)
    Recherche.place(x=300, y=0)
    #Button stock :
    stock=Button(top, text="Stock",font=("Courrier",20),bg="blue", fg='white', command=stock)
    stock.place(x=500,y=0)
    #Button quitter :
    quitter=Button(top,text="Quitter",font=("Courrier",20),bg="red",fg="white",command=top.quit)
    quitter.place(x=650,y=0)

#La commande du button stock golbal :
def stockg():
    #La fonction du boutton recherche : 
    def Recherche():
        #La fonction du button rechercher : 
        #global entryClient, entryType, entryComptage, entryComptageClient, entryComptageType, entryDate, entryHeure 
        def action():
            client=entryClient.get()
            typ=entryType.get()
            if client not in client_base and typ in type_base:
                messagebox.showerror("Ereur client","Veuillez entrez un client existant")
            if typ not in type_base and client in client_base:
                messagebox.showerror("Ereur type","Veuillez entrez un type existant")
            if typ not in type_base and client not in client_base:
                messagebox.showerror("Ereur client et type","Veuillez entrez un client et un type existant")
            k=False
            for bidon in list_bidon_stock:
                if bidon["client"]==client and bidon["type"]==typ:
                    bidon_corr=bidon
                    comptage=bidon_corr["reste"]
                    k=True
                    break
            if k==False:
                comptage=0
            comptage_client=0
            for bidon in list_bidon_stock:
                if bidon["client"]==client:
                    comptage_client+=bidon["reste"]
            comptage_type=0
            for bidon in list_bidon_stock:
                if bidon["type"]==typ:
                    comptage_type+=bidon["reste"]
            

            Date=datetime.date.today()
            Heure=espace(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) 
            entryComptage.delete(0, END)
            entryComptageClient.delete(0,END)
            entryComptageType.delete(0,END)
            entryDate.delete(0, END)
            entryHeure.delete(0, END)
            entryComptage.insert(0, comptage)
            entryComptageClient.insert(0, comptage_client)
            entryComptageType.insert(0, comptage_type)
            entryDate.insert(0, Date)
            entryHeure.insert(0, Heure)
        #Fenetre du button recherche dans l'atelier 1 :
        top1=Tk()
        top1.title("Recherche dans le stock")
        top1.geometry("1080x720")
        top1.iconbitmap('logo.ico')
        top1.configure(background="#41B77F")
        #Client
        lablClient=Label(top1, text='Client : ')
        lablClient.place(x=400, y=100)
        entryClient=Entry(top1)
        entryClient.place(x=600, y=100)
        #Type
        lablType=Label(top1, text='Type : ')
        lablType.place(x=400,y=150)
        entryType=Entry(top1)
        entryType.place(x=600,y=150)
        #Comptage
        lablComptage=Label(top1, text='Comptage  :')
        lablComptage.place(x=400,y=200)
        entryComptage=Entry(top1,fg="red")
        entryComptage.place(x=600,y=200)
        #Total comtage par client
        lablComptageClient=Label(top1, text='Comptage par client :')
        lablComptageClient.place(x=400,y=250)
        entryComptageClient=Entry(top1,fg="red")
        entryComptageClient.place(x=600,y=250)
        #Total comptage par type
        lablComptageType=Label(top1, text='Comptage par type :')
        lablComptageType.place(x=400,y=300)
        entryComptageType=Entry(top1,fg="red")
        entryComptageType.place(x=600,y=300)
        #Date 
        lablDate=Label(top1, text='Date  :')
        lablDate.place(x=400,y=350)
        entryDate=Entry(top1,fg="red")
        entryDate.place(x=600,y=350)
        #Heure
        lablHeure=Label(top1, text='Heure  :')
        lablHeure.place(x=400,y=400)
        entryHeure=Entry(top1,fg="red")
        entryHeure.place(x=600,y=400)
        #Button recherche
        rechercher=Button(top1, text="Rechercher", font=("Courrier",20), bg="blue", fg='white', command=action)
        rechercher.place(x=600,y=450)
        #Button quitter : 
        quitter=Button(top1, text="Quitter",font=('Courrier',20),bg="red",fg="white",command=top1.quit)
        quitter.place(x=350,y=450)
    def stock():
        #fonction du client A : 
        def A():
            topA=Tk()
            topA.title("déchets du client A dans le stock")
            topA.geometry("1350x1350")
            topA.iconbitmap('logo.ico')
            topA.configure(background="#41B77F")
            #Time :
            Label(topA,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topA,text="l'état du stock du client A dans le stock",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topA,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topA,text="A",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topA,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientA=0
            for bidon in list_bidon_stock:
                if bidon["client"]=='A':
                    comptage_clientA+=bidon["reste"]
            Label(topA,text=comptage_clientA,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topA,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="A" and bidon["type"]=="solvant":
                   comptage_solvantA=bidon["reste"]
                   k=True
                   break
            if k==False:
                comptage_solvantA=0
            Label(topA,text=comptage_solvantA,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topA,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="A" and bidon["type"]=="liquide":
                   comptage_liquideA=bidon["reste"]
                   l=True
                   break
            if l==False :
                comptage_liquideA=0
            Label(topA,text=comptage_liquideA,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topA,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="A" and bidon["type"]=="solide":
                   comptage_solideA=bidon["reste"]
                   s=True
                   break
            if s==False :
                comptage_solideA=0 
            Label(topA,text=comptage_solideA,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #fonction du client B : 
        def B():
            topB=Tk()
            topB.title("Déchets du client B dans le stock ")
            topB.geometry("1350x1350")
            topB.iconbitmap('logo.ico')
            topB.configure(background="#41B77F")
            #Time :
            Label(topB,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topB,text="l'état du stock du client B dans le stock",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topB,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topB,text="B",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topB,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientB=0
            for bidon in list_bidon_stock:
                if bidon["client"]=='B':
                    comptage_clientB+=bidon["reste"]
            Label(topB,text=comptage_clientB,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topB,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="B" and bidon["type"]=="solvant":
                   comptage_solvantB=bidon["reste"]
                   k=True
                   break
            if k==False:
                comptage_solvantB=0
            Label(topB,text=comptage_solvantB,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topB,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="B" and bidon["type"]=="liquide":
                   comptage_liquideB=bidon["reste"]
                   l=True
                   break
            if l==False :
                comptage_liquideB=0
            Label(topB,text=comptage_liquideB,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topB,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="B" and bidon["type"]=="solide":
                   comptage_solideB=bidon["reste"]
                   s=True
                   break
            if s==False :
                comptage_solideB=0 
            Label(topB,text=comptage_solideB,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #fonction du client C : 
        def C():
            topC=Tk()
            topC.title("Déchets du client C dans le stock")
            topC.geometry("1350x1350")
            topC.iconbitmap('logo.ico')
            topC.configure(background="#41B77F")
            #Time :
            Label(topC,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topC,text="l'état du stock du client C dans le stock",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topC,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topC,text="C",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topC,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientC=0
            for bidon in list_bidon_stock:
                if bidon["client"]=='C':
                    comptage_clientC+=bidon["reste"]
            Label(topC,text=comptage_clientC,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topC,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="C" and bidon["type"]=="solvant":
                   comptage_solvantC=bidon["reste"]
                   k=True
                   break
            if k==False:
                comptage_solvantC=0
            Label(topC,text=comptage_solvantC,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topC,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="C" and bidon["type"]=="liquide":
                   comptage_liquideC=bidon["reste"]
                   l=True
                   break
            if l==False :
                comptage_liquideC=0
            Label(topC,text=comptage_liquideC,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topC,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="C" and bidon["type"]=="solide":
                   comptage_solideC=bidon["reste"]
                   s=True
                   break
            if s==False :
                comptage_solideC=0 
            Label(topC,text=comptage_solideC,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #fonction du client D : 
        def D():
            topD=Tk()
            topD.title("Déchets du client D dans le stock ")
            topD.geometry("1350x1350")
            topD.iconbitmap('logo.ico')
            topD.configure(background="#41B77F")
            #Time :
            Label(topD,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topD,text="l'état du stock du client D dans l'atelier 2",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topD,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topD,text="D",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topD,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientD=0
            for bidon in list_bidon_stock:
                if bidon["client"]=='D':
                    comptage_clientD+=bidon["reste"]
            Label(topD,text=comptage_clientD,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topD,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="D" and bidon["type"]=="solvant":
                   comptage_solvantD=bidon["reste"]
                   k=True
                   break
            if k==False:
                comptage_solvantD=0
            Label(topD,text=comptage_solvantD,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topD,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="D" and bidon["type"]=="liquide":
                   comptage_liquideD=bidon["reste"]
                   l=True
                   break
            if l==False :
                comptage_liquideD=0
            Label(topD,text=comptage_liquideD,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topD,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="D" and bidon["type"]=="solide":
                   comptage_solideD=bidon["reste"]
                   s=True
                   break
            if s==False :
                comptage_solideD=0 
            Label(topD,text=comptage_solideD,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #fonction du client E : 
        def E():
            topE=Tk()
            topE.title("Déchets du client E dans le stock")
            topE.geometry("1350x1350")
            topE.iconbitmap('logo.ico')
            topE.configure(background="#41B77F")
            #Time :
            Label(topE,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topE,text="l'état du stock du client E dans le stock ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topE,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topE,text="E",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topE,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientE=0
            for bidon in list_bidon_stock:
                if bidon["client"]=='E':
                    comptage_clientE+=bidon["reste"]
            Label(topE,text=comptage_clientE,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topE,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="E" and bidon["type"]=="solvant":
                   comptage_solvantE=bidon["reste"]
                   k=True
                   break
            if k==False:
                comptage_solvantE=0
            Label(topE,text=comptage_solvantE,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topE,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="E" and bidon["type"]=="liquide":
                   comptage_liquideE=bidon["reste"]
                   l=True
                   break
            if l==False :
                comptage_liquideE=0
            Label(topE,text=comptage_liquideE,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topE,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="E" and bidon["type"]=="solide":
                   comptage_solideE=bidon["reste"]
                   s=True
                   break
            if s==False :
                comptage_solideE=0 
            Label(topE,text=comptage_solideE,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #fonction du client F : 
        def F():
            topF=Tk()
            topF.title("Déchets du client F dans le stock")
            topF.geometry("1350x1350")
            topF.iconbitmap('logo.ico')
            topF.configure(background="#41B77F")
            #Time :
            Label(topF,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topF,text="l'état du stock du client F dans le stock",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topF,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topF,text="F",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topF,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientF=0
            for bidon in list_bidon_stock:
                if bidon["client"]=='F':
                    comptage_clientF+=bidon["reste"]
            Label(topF,text=comptage_clientF,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topF,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="F" and bidon["type"]=="solvant":
                   comptage_solvantF=bidon["reste"]
                   k=True
                   break
            if k==False:
                comptage_solvantF=0
            Label(topF,text=comptage_solvantF,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topF,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="F" and bidon["type"]=="liquide":
                   comptage_liquideF=bidon["reste"]
                   l=True
                   break
            if l==False :
                comptage_liquideF=0
            Label(topF,text=comptage_liquideF,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topF,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="F" and bidon["type"]=="solide":
                   comptage_solideF=bidon["reste"]
                   s=True
                   break
            if s==False :
                comptage_solideF=0 
            Label(topF,text=comptage_solideF,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #fonction du client G : 
        def G():
            topG=Tk()
            topG.title("Déchets du client G dans le stock")
            topG.geometry("1350x1350")
            topG.iconbitmap('logo.ico')
            topG.configure(background="#41B77F")
            #Time :
            Label(topG,text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),font=("Courrier",20),bg="#41B77F",fg="red").place(x=0,y=0)
            #Création de cartes clients :
            Label(topG,text="l'état du stock du client G dans le stock",font=("Courrier",40),bg="#41B77F",fg="white").place(x=50,y=50)
            
            #nom du client : 
            Label(topG,text="Nom du client :",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=150)
            Label(topG,text="G",font=("Courrier",40),bg="#41B77F",fg="black").place(x=600,y=150)
            #Comptage total :
            Label(topG,text="Comptage total : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=250)
            comptage_clientG=0
            for bidon in list_bidon_stock:
                if bidon["client"]=='G':
                    comptage_clientG+=bidon["reste"]
            Label(topG,text=comptage_clientG,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=250)
            #Comptage solvant :
            Label(topG,text="solvants : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=350)
            k=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="G" and bidon["type"]=="solvant":
                   comptage_solvantG=bidon["reste"]
                   k=True
                   break
            if k==False:
                comptage_solvantG=0
            Label(topG,text=comptage_solvantG,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=350)
            #Comptage liquide :
            Label(topG,text="Liquides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=450)
            l=False
            for bidon in list_bidon_stock:
                if bidon["client"]=="G" and bidon["type"]=="liquide":
                   comptage_liquideG=bidon["reste"]
                   l=True
                   break
            if l==False :
                comptage_liquideG=0
            Label(topG,text=comptage_liquideG,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=450)
            #Comptage solide :
            Label(topG,text="Solides : ",font=("Courrier",40),bg="#41B77F",fg="white").place(x=150,y=550)
            s=False
            for bidon in list_bidon_entre_stock:
                if bidon["client"]=="G" and bidon["type"]=="solide":
                   comptage_solideG=bidon["reste"]
                   s=True
                   break
            if s==False :
                comptage_solideG=0 
            Label(topG,text=comptage_solideG,font=("Courrier",40),bg="#41B77F",fg="red").place(x=600,y=550)
        #Fentere de stock : 
        top2=Tk()
        top2.title("stock ")
        top2.geometry("1080x720")
        top2.iconbitmap('logo.ico')
        top2.configure(background="#41B77F")
        #Création des textes :
        texte_stock1=Label(top2,text="Gestion des clients dans le stock",font=("Courrier",40),bg="#41B77F",fg="white")
        texte_stock1.place(x=150,y=50)
       
        #Création des bouttons :
        #A
        Button(top2,text="A",font=('Courrier',25),bg="black",fg="white",command=A).place(x=50,y=300)
        #B
        Button(top2,text="B",font=('Courrier',25),bg="black",fg="white",command=B).place(x=300,y=300)
        #C
        Button(top2,text="C",font=('Courrier',25),bg="black",fg="white",command=C).place(x=550,y=300)
        #D
        Button(top2,text="D",font=('Courrier',25),bg="black",fg="white",command=D).place(x=800,y=300)
        #E
        Button(top2,text="E",font=('Courrier',25),bg="black",fg="white",command=E).place(x=50,y=500)
        #F
        Button(top2,text="F",font=('Courrier',25),bg="black",fg="white",command=F).place(x=300,y=500)
        #G
        Button(top2,text="G",font=('Courrier',25),bg="black",fg="white",command=G).place(x=550,y=500)   
    top=Tk()
    top.title("Stock")
    top.geometry("1080x720")
    top.iconbitmap('logo.ico')
    top.configure(background="#41B77F")
    #Ajouter texte :
    label_title=Label(top, text="Gestion du Stock ", font=("Courrier",60),bg="#41B77F", fg='white')
    label_title.pack(expand=YES)
    #Recherche Button : 
    Recherche=Button(top, text="Recherche",font=("Courrier",20),bg="blue", fg='white', command=Recherche)
    Recherche.place(x=300, y=0)
    #Button stock :
    stock=Button(top, text="Stock",font=("Courrier",20),bg="blue", fg='white', command=stock)
    stock.place(x=500,y=0)
    #Button quitter :
    quitter=Button(top,text="Quitter",font=("Courrier",20),bg="red",fg="white",command=top.quit)
    quitter.place(x=650,y=0)

#Fenetre des bases de données : 

#Fenetre principale : 
fen=Tk()
fen.title("Interface administrateur")
fen.geometry("1080x720")
fen.minsize(480, 360)
fen.iconbitmap("logo.ico")
fen.config(background="#41B77F")
#Aelier 1 Button : 
Atelier1=Button(fen, text="Atelier1",font=("Courrier",20),bg="yellow", fg='black', command=Atelier1)
Atelier1.place(x=250, y=0)
#Aelier 2 Button : 
Atelier2=Button(fen, text="Atelier2",font=("Courrier",20),bg="yellow", fg='black', command=Atelier2)
Atelier2.place(x=400, y=0)
#stock Button : 
stock=Button(fen, text="Stock",font=("Courrier",20),bg="yellow", fg='black', command=stockg)
stock.place(x=550, y=0)
#quit Button : 
quitter=Button(fen, text="Quitter",font=("Courrier",20),bg="red", fg='black', command=fen.quit)
quitter.place(x=700, y=0)
#Base de données existant : 
#Créer un frame (boite):
frame=Frame( fen, bg="#41B77F",bd=1, relief=SUNKEN)
#Ajouter texte :
label_title=Label(frame, text="Bienvenue sur GEOApp", font=("Courrier",40),bg="#41B77F", fg='white')
label_title.pack(expand=YES)
#ajouter autre texte : 
label_subtitle=Label(frame, text="Une application qui vous garantit une meilleur gestion de stock", font=("Courrier",25),bg="#41B77F", fg='white')
label_subtitle.pack(expand=YES)
#Ajouter la boite (frame):
frame.pack(expand=YES)

mainloop()
entre_stock.close()
sortie_stock.close()
entre1.close()
sortie1.close()
entre2.close()
sortie2.close()