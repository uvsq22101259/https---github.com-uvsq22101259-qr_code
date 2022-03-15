# noir = 1
# blanc  = 0
from tracemalloc import stop
import PIL as pil
from PIL import Image
from PIL import ImageTk 


def nbrCol(matrice):
    return(len(matrice[0]))


def nbrLig(matrice):
    return len(matrice)


def saving(matPix, filename):#sauvegarde l'image contenue dans matpix dans le fichier filename
							 #utiliser une extension png pour que la fonction fonctionne sans perte d'information
    toSave=pil.Image.new(mode = "1", size = (nbrCol(matPix),nbrLig(matPix)))
    for i in range(nbrLig(matPix)):
        for j in range(nbrCol(matPix)):
            toSave.putpixel((j,i),matPix[i][j])
    toSave.save(filename)


def loading(filename):#charge le fichier image filename et renvoie une matrice de 0 et de 1 qui représente 
					  #l'image en noir et blanc
    toLoad=pil.Image.open(filename)
    mat=[[0]*toLoad.size[0] for k in range(toLoad.size[1])]
    for i in range(toLoad.size[1]):
        for j in range(toLoad.size[0]):
            mat[i][j]= 0 if toLoad.getpixel((j,i)) == 0 else 1
    return mat


def squellette():
    matrice =loading("coin.png")
    return matrice


def chek_coin(matrice):
    matrice = loading(matrice)
    test = squellette()
    chek = 0
    # print(matrice[0][17:])
    # print(test[0][: :-1])
    for i in range (8):
        if matrice[i][:8] == test[i] and matrice[-i+(-1)][:8] == test[i] and matrice[i][17:] == test[i] [: :-1] :
            chek += 1
            pass
        else: 
            print("ce n'est pa un bon carré" )
            break
    if chek == 8:        
        print("les qr code est dans la bonne position")


def rotation(matrice):
    matrice = loading(matrice)
    matrice_retourner = []
    




rotation("qr_code_ssfiltre_ascii_rotation.png")
