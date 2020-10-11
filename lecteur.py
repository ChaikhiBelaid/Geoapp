import xlrd
#import xlwt
texte=open("entre.txt", "r")
codes_texte=texte.readlines()
codes_barre=[]
for i in range(len(codes_texte)-1):
    codes_barre.append(codes_texte[i][:-1])
doc=xlrd.open_workbook("base de données.xlsx")
feuille_1 = doc.sheet_by_index(0)
rows = feuille_1.nrows
codes_base=[]
for i in range(1,rows):
    cellule = feuille_1.cell_value(rowx=i, colx=0)
    codes_base.append(cellule)
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
"""print([1,1,1,0,2,3,1,0,0,3,4,0,3])
print(nombre_rep([1,1,1,0,2,3,1,0,0,3,4,0,3]))"""


list_bidon=[]
print("codes barre = ",codes_barre)
print("codes base = ", codes_base)
codes_barre_clean=nombre_rep(codes_barre)
print("code barre clean = ",codes_barre_clean)
for code in codes_barre_clean :
    if code in codes_base:       
        client_bidon = feuille_1.cell_value(rowx=codes_base.index(code)+1, colx=1)
        type_bidon = feuille_1.cell_value(rowx=codes_base.index(code)+1, colx=2)
        comptage=codes_barre.count(code)
        bidon={"code":code, "client":client_bidon, "type":int(type_bidon),"comptage":comptage}
        list_bidon.append(bidon) 
print("liste des bidons = ", list_bidon)
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
texte.close()