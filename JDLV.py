import matplotlib.pyplot as plt
from time import time



'''automate cellulaire test'''
from time import sleep
from random import randint

def dessin(A):
    for i in range (len(A)):
        print('')
        for j in range(len(A)):
            if A[i][j]==1:
                print("■",end=' ')
            else:
                print("☐",end=' ')
    print('')
def temps(n):
    return "{}h {}m {}s".format(int((((n-n%60)/60)-(((n-n%60)/60)%60))/60),int(((n-n%60)/60)%60),int(n%60))
def rand_mat(n):
    return [[randint(0,1) for i in range(n)]for i in range(n)]
def zeros(n):
    return [[0 for i in range(n)] for i in range(n)]
def voisins(A,i,j):
    c=0
    if A[i][j]==1:
        c=-1
    if i!=len(A)-1 and i!=0 and j!=0 and j!=len(A)-1:    #Case au milieu de tout
        for k in range(0,3):
            for l in range(0,3):
                if A[i+k-1][j+l-1]==1:
                    c+=1
    elif i==len(A)-1 and j==len(A)-1:           #Case en bas à droite
        for k in range(0,2):
            for l in range(0,2):
                if A[i-k][j-l]==1:
                    c+=1
    elif i==len(A)-1 and j==0:              #Case en bas à gauche
        for k in range(0,2):
            for l in range(0,2):
                if A[i-k][j+l]==1:
                    c+=1
    elif i==0 and j==len(A)-1:              #Case en haut à droite
        for k in range(0,2):
            for l in range(0,2):
                if A[i+k][j-l]==1:
                    c+=1
    elif i==0 and j==0:                 #Case en haut à gauche
        for k in range(0,2):
            for l in range(0,2):
                if A[i+k][j+l]==1:
                    c+=1
    elif i==len(A)-1:                   #dernière ligne (bords exclus)
        for l in range(0,3):
            for k in range(0,2):
                if A[i+k-1][j+l-1]==1:
                    c+=1
    elif j==len(A)-1:                   #dernière colonne (bords exclus)
        for l in range(0,3):
            for k in range(0,2):
                if A[i+l-1][j+k-1]==1:
                    c+=1
    elif i==0:                          #première ligne (bords exclus)
        for l in range(0,3):
            for k in range(0,2):
                if A[k][j+l-1]==1:
                    c+=1
    elif j==0:                          #première colonne (bords exclus)
        for l in range(0,3):
            for k in range(0,2):
                if A[i+l-1][k]==1:
                    c+=1
    else:
        print("ERROR pour A",i,j)
    #print("A {}{} : {}".format(i,j,c))
    return c
def somme(A):
    c=0
    for i in A:
        for j in i:
            c+=j
    return c




### Début programme ###

def jdlv(t,n,g,d):
    """Variables:\n
    t: Taille de la matrice comportant les cellules
    n: Nombre de générations
    g: Nombre de générations par seconde
    d: 1 pour afficher la simulation, 0 sinon
    
    JDLV:
    - lance une simulation du jeu de la vie
    - affiche le graphe 'Nombre de cellules vivantes par génération'
    """
    
    A=rand_mat(t)
    B=zeros(t)
    C=zeros(t)
    x=[]
    y=[]
    a=1
    ref=0
    t1=time()
    
    for k in range(n):
        if d==1:
            dessin(A)
            sleep(1/g)
        else:
            t2=time()
            if a and ref>0:
                print("\n\nPrédiction: ~",temps(ref*n),"\n\n")
                a=0
            if int(t2-t1)>=int(ref)+1:
                print(temps(t2-t1)," :",k*100/n,"% complete")
            
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i][j]==0 and voisins(A,i,j)==3:
                    B[i][j]=1
                elif A[i][j]==1 and (voisins(A,i,j)==2 or voisins(A,i,j)==3):
                    B[i][j]=1
                else:
                    B[i][j]=0
        if (k/5)%1==0:
            for p in range(len(A)):
                C[p]=A[p][:]
        for p in range(len(A)):             #A=B
            A[p]=B[p][:]
        if A==C:
            break
        y.append(somme(A))
        x.append(k+1)
        ref=t2-t1
        
    print("100.0 % complete")
    plt.plot(x,y,c='r')
    plt.xlabel("N° génération")
    plt.ylabel("Nombre de cellules vivantes")
    plt.show()