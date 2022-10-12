#Aqui escrevemos as funções que serão utilizadas para descobrir o DETERMINANTE
def Determinante2x2(matriz,Determinante):
    Determinante=(matriz[0][0]*matriz[1][1])-(matriz[0][1]*matriz[1][0])
    return Determinante
def Determinante3x3(matriz,Determinante):
    diagonalPositiva=(matriz[0][0]*matriz[1][1]*matriz[2][2])+(matriz[2][0]*matriz[0][1]*matriz[1][2])+(matriz[1][0]*matriz[2][1]*matriz[0][2])
    diagonalNegativa=(matriz[2][2]*matriz[0][1]*matriz[1][0])+(matriz[0][2]*matriz[1][1]*matriz[2][0])+(matriz[1][2]*matriz[2][1]*matriz[0][0])
    Determinante=diagonalPositiva-diagonalNegativa
    return Determinante
def Determinante4x4(matriz,Determinante):
    diagonalPositiva1=(matriz[1][1]*matriz[2][2]*matriz[3][3])+(matriz[3][1]*matriz[1][2]*matriz[2][3])+(matriz[2][1]*matriz[3][2]*matriz[1][3])
    diagonalNegativa1=(matriz[3][3]*matriz[1][2]*matriz[2][1])+(matriz[1][3]*matriz[2][2]*matriz[3][1])+(matriz[2][3]*matriz[3][2]*matriz[1][1])
    Cofator1=diagonalPositiva1-diagonalNegativa1
    diagonalPositiva2=(matriz[0][1]*matriz[2][2]*matriz[3][3])+(matriz[3][1]*matriz[0][2]*matriz[2][3])+(matriz[2][1]*matriz[3][2]*matriz[0][3])
    diagonalNegativa2=(matriz[3][3]*matriz[0][2]*matriz[2][1])+(matriz[0][3]*matriz[2][2]*matriz[3][1])+(matriz[2][3]*matriz[3][2]*matriz[0][1])
    Cofator2=diagonalPositiva2-diagonalNegativa2
    diagonalPositiva3=(matriz[0][1]*matriz[1][2]*matriz[3][3])+(matriz[3][1]*matriz[0][2]*matriz[1][3])+(matriz[1][1]*matriz[3][2]*matriz[0][3])
    diagonalNegativa3=(matriz[3][3]*matriz[0][2]*matriz[1][1])+(matriz[0][3]*matriz[1][2]*matriz[3][1])+(matriz[1][3]*matriz[3][2]*matriz[0][1])
    Cofator3=diagonalPositiva3-diagonalNegativa3
    diagonalPositiva4=(matriz[0][1]*matriz[1][2]*matriz[2][3])+(matriz[2][1]*matriz[0][2]*matriz[1][3])+(matriz[1][1]*matriz[2][2]*matriz[0][3])
    diagonalNegativa4=(matriz[2][3]*matriz[0][2]*matriz[1][1])+(matriz[0][3]*matriz[1][2]*matriz[2][1])+(matriz[1][3]*matriz[2][2]*matriz[0][1])
    Cofator4=diagonalPositiva4-diagonalNegativa4
    Determinante=(matriz[0][0]*Cofator1)-(matriz[1][0]*Cofator2)+(matriz[2][0]*Cofator3)-(matriz[3][0]*Cofator4)
    return Determinante
#Aqui escrevemos as funções que serão utilizadas para descobrir a MATRIZ INVERSA
def MatrizInversa1x1(matrizinversa1,matriz):
    if matriz[0]>=0:
        matrizinversa1.append(1/matriz[0])
    else:
        matrizinversa1.append(-1/matriz[0])
    return matrizinversa1
def MatrizInversa2x2(matrizinversa2,matriz,Determinante):
    matrizinversa2[0][0]=matriz[1][1]/Determinante
    matrizinversa2[0][1]=-matriz[0][1]/Determinante
    matrizinversa2[1][0]=-matriz[1][0]/Determinante
    matrizinversa2[1][1]=matriz[0][0]/Determinante
    return matrizinversa2
def MatrizInversa3x3(matrizinversa3,matriz,Determinante):
    matrizinversa3[0][0]=((matriz[1][1]*matriz[2][2])-(matriz[1][2]*matriz[2][1]))/Determinante
    matrizinversa3[0][1]=-((matriz[0][1]*matriz[2][2])-(matriz[0][2]*matriz[2][1]))/Determinante
    matrizinversa3[0][2]=((matriz[0][1]*matriz[1][2])-(matriz[0][2]*matriz[1][1]))/Determinante
    matrizinversa3[1][0]=-((matriz[1][0]*matriz[2][2])-(matriz[1][2]*matriz[2][0]))/Determinante
    matrizinversa3[1][1]=((matriz[0][0]*matriz[2][2])-(matriz[0][2]*matriz[2][0]))/Determinante
    matrizinversa3[1][2]=-((matriz[0][0]*matriz[1][2])-(matriz[0][2]*matriz[1][0]))/Determinante
    matrizinversa3[2][0]=((matriz[1][0]*matriz[2][1])-(matriz[1][1]*matriz[2][0]))/Determinante
    matrizinversa3[2][1]=-((matriz[0][0]*matriz[2][1])-(matriz[0][1]*matriz[2][0]))/Determinante
    matrizinversa3[2][2]=((matriz[0][0]*matriz[1][1])-(matriz[0][1]*matriz[1][0]))/Determinante
    return matrizinversa3
def MatrizInversa4x4(matrizinversa4,matriz,Determinante):
    matrizinversa4[0][0]=((matriz[3][1]*matriz[1][2]*matriz[2][3])+(matriz[1][1]*matriz[2][2]*matriz[3][3])+(matriz[2][1]*matriz[3][2]*matriz[1][3])-(matriz[3][3]*matriz[1][2]*matriz[2][1])-(matriz[1][3]*matriz[2][2]*matriz[3][1])-(matriz[2][3]*matriz[3][2]*matriz[1][1]))/Determinante
    matrizinversa4[1][0]=-((matriz[3][0]*matriz[1][2]*matriz[2][3])+(matriz[1][0]*matriz[2][2]*matriz[3][3])+(matriz[2][0]*matriz[3][2]*matriz[1][3])-(matriz[3][3]*matriz[1][2]*matriz[2][0])-(matriz[1][3]*matriz[2][2]*matriz[3][0])-(matriz[2][3]*matriz[3][2]*matriz[1][0]))/Determinante
    matrizinversa4[2][0]=((matriz[3][0]*matriz[1][1]*matriz[2][3])+(matriz[1][0]*matriz[2][1]*matriz[3][3])+(matriz[2][0]*matriz[3][1]*matriz[1][3])-(matriz[3][3]*matriz[1][1]*matriz[2][0])-(matriz[1][3]*matriz[2][1]*matriz[3][0])-(matriz[2][3]*matriz[3][1]*matriz[1][0]))/Determinante
    matrizinversa4[3][0]=-((matriz[3][0]*matriz[1][1]*matriz[2][2])+(matriz[1][0]*matriz[2][1]*matriz[3][2])+(matriz[2][0]*matriz[3][1]*matriz[1][2])-(matriz[3][2]*matriz[1][1]*matriz[2][0])-(matriz[1][2]*matriz[2][1]*matriz[3][0])-(matriz[2][2]*matriz[3][1]*matriz[1][0]))/Determinante
    matrizinversa4[0][1]=-((matriz[3][1]*matriz[0][2]*matriz[2][3])+(matriz[0][1]*matriz[2][2]*matriz[3][3])+(matriz[2][1]*matriz[3][2]*matriz[0][3])-(matriz[3][3]*matriz[0][2]*matriz[2][1])-(matriz[0][3]*matriz[2][2]*matriz[3][1])-(matriz[2][3]*matriz[3][2]*matriz[0][1]))/Determinante
    matrizinversa4[1][1]=((matriz[3][0]*matriz[0][2]*matriz[2][3])+(matriz[0][0]*matriz[2][2]*matriz[3][3])+(matriz[2][0]*matriz[3][2]*matriz[0][3])-(matriz[3][3]*matriz[0][2]*matriz[2][0])-(matriz[0][3]*matriz[2][2]*matriz[3][0])-(matriz[2][3]*matriz[3][2]*matriz[0][0]))/Determinante
    matrizinversa4[2][1]=-((matriz[3][0]*matriz[0][1]*matriz[2][3])+(matriz[0][0]*matriz[2][1]*matriz[3][3])+(matriz[2][0]*matriz[3][1]*matriz[0][3])-(matriz[3][3]*matriz[0][1]*matriz[2][0])-(matriz[0][3]*matriz[2][1]*matriz[3][0])-(matriz[2][3]*matriz[3][1]*matriz[0][0]))/Determinante
    matrizinversa4[3][1]=((matriz[3][0]*matriz[0][1]*matriz[2][2])+(matriz[0][0]*matriz[2][1]*matriz[3][2])+(matriz[2][0]*matriz[3][1]*matriz[0][2])-(matriz[3][2]*matriz[0][1]*matriz[2][0])-(matriz[0][2]*matriz[2][1]*matriz[3][0])-(matriz[2][2]*matriz[3][1]*matriz[0][0]))/Determinante
    matrizinversa4[0][2]=((matriz[3][1]*matriz[0][2]*matriz[1][3])+(matriz[0][1]*matriz[1][2]*matriz[3][3])+(matriz[1][1]*matriz[3][2]*matriz[0][3])-(matriz[3][3]*matriz[0][2]*matriz[1][1])-(matriz[0][3]*matriz[1][2]*matriz[3][1])-(matriz[1][3]*matriz[3][2]*matriz[0][1]))/Determinante
    matrizinversa4[1][2]=-((matriz[3][0]*matriz[0][2]*matriz[1][3])+(matriz[0][0]*matriz[1][2]*matriz[3][3])+(matriz[1][0]*matriz[3][2]*matriz[0][3])-(matriz[3][3]*matriz[0][2]*matriz[1][0])-(matriz[0][3]*matriz[1][2]*matriz[3][0])-(matriz[1][3]*matriz[3][2]*matriz[0][0]))/Determinante
    matrizinversa4[2][2]=((matriz[3][0]*matriz[0][1]*matriz[1][3])+(matriz[0][0]*matriz[1][1]*matriz[3][3])+(matriz[1][0]*matriz[3][1]*matriz[0][3])-(matriz[3][3]*matriz[0][1]*matriz[1][0])-(matriz[0][3]*matriz[1][1]*matriz[3][0])-(matriz[1][3]*matriz[3][1]*matriz[0][0]))/Determinante
    matrizinversa4[3][2]=-((matriz[3][0]*matriz[0][1]*matriz[1][2])+(matriz[0][0]*matriz[1][1]*matriz[3][2])+(matriz[1][0]*matriz[3][1]*matriz[0][2])-(matriz[3][2]*matriz[0][1]*matriz[1][0])-(matriz[0][2]*matriz[1][1]*matriz[3][0])-(matriz[1][2]*matriz[3][1]*matriz[0][0]))/Determinante
    matrizinversa4[0][3]=-((matriz[2][1]*matriz[0][2]*matriz[1][3])+(matriz[0][1]*matriz[1][2]*matriz[2][3])+(matriz[1][1]*matriz[2][2]*matriz[0][3])-(matriz[2][3]*matriz[0][2]*matriz[1][1])-(matriz[0][3]*matriz[1][2]*matriz[2][1])-(matriz[1][3]*matriz[2][2]*matriz[0][1]))/Determinante
    matrizinversa4[1][3]=((matriz[2][0]*matriz[0][2]*matriz[1][3])+(matriz[0][0]*matriz[1][2]*matriz[2][3])+(matriz[1][0]*matriz[2][2]*matriz[0][3])-(matriz[2][3]*matriz[0][2]*matriz[1][0])-(matriz[0][3]*matriz[1][2]*matriz[2][0])-(matriz[1][3]*matriz[2][2]*matriz[0][0]))/Determinante
    matrizinversa4[2][3]=-((matriz[2][0]*matriz[0][1]*matriz[1][3])+(matriz[0][0]*matriz[1][1]*matriz[2][3])+(matriz[1][0]*matriz[2][1]*matriz[0][3])-(matriz[2][3]*matriz[0][1]*matriz[1][0])-(matriz[0][3]*matriz[1][1]*matriz[2][0])-(matriz[1][3]*matriz[2][1]*matriz[0][0]))/Determinante
    matrizinversa4[3][3]=((matriz[2][0]*matriz[0][1]*matriz[1][2])+(matriz[0][0]*matriz[1][1]*matriz[2][2])+(matriz[1][0]*matriz[2][1]*matriz[0][2])-(matriz[2][2]*matriz[0][1]*matriz[1][0])-(matriz[0][2]*matriz[1][1]*matriz[2][0])-(matriz[1][2]*matriz[2][1]*matriz[0][0]))/Determinante
    return matrizinversa4      
Menu=0
while Menu!=4:
    Menu=int(input("1.Determinante da matriz\n2.Mudança de base\n3.Matriz inversa\n4.Sair\nDigite qual opção você deseja: "))
    print("-"*20)
    matriz1=[]
    matriz2=[[],[]]
    matriz3=[[],[],[]]
    matriz4=[[],[],[],[]]
    vetorA = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    a = 0
    vetorB = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    b = 0
    matriz_inversa =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    matriz_mudança_base =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    matrizinversa1=[]
    matrizinversa2=[[0,0],[0,0]]
    matrizinversa3=[[0,0,0],[0,0,0],[0,0,0]]
    matrizinversa4=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    x=0
    Determinante=0        
    if Menu==4:
        print("Programa encerrado")
        print("-"*20)
    elif Menu==1 or Menu==3:
        while x==0:
            Random=int(input("1.Matriz aleatória\n2.Matriz escrita manualmente\nDigite qual opção você deseja: "))
            print("-"*20)
            if Random==1 or Random==2:
                x=1
            else:
                print("Comando inválido")
                print("-"*20)  
        if Random==1:
            import random
            tamanho=random.randint(1,4)
            if tamanho==1:
                ale=random.randint(0,100)
                matriz1.append(ale)
                matriz=matriz1
            elif tamanho==2:
                for i in range(2):
                    for j in range(2):
                        ale=random.randint(0,100)
                        matriz2[i].append(ale)
                matriz=matriz2
            elif tamanho==3:
                for i in range(3):
                    for j in range(3):
                        ale=random.randint(0,100)
                        matriz3[i].append(ale)
                matriz=matriz3
            elif tamanho==4:
                for i in range(4):
                    for j in range(4):
                        ale=random.randint(0,100)
                        matriz4[i].append(ale)
                matriz=matriz4 
        elif Random==2:
            while x==1:
                tamanho=int(input("1.1x1\n2.2x2\n3.3x3\n4.4x4\nDigite o número correspondente ao tamanho da sua matriz: "))
                print("-"*20)  
                if tamanho==1 or tamanho==2 or tamanho==3 or tamanho==4:
                    x=0
                else:
                    print("Comando inválido")
                    print("-"*20)
            if tamanho==1:
                v=int(input("Digite o valor: "))
                matriz1.append(v)
                matriz=matriz1
            elif tamanho==2:
                for i in range (2):
                    for j in range(2):
                        print("Linha",i+1,"Coluna:",j+1)               
                        v=int(input("Digite o valor para essa posição: "))
                        print("***")
                        matriz2[i].append(v)    
                matriz=matriz2                                                    
            elif tamanho==3:
                for i in range (3):
                    for j in range(3):
                        print("Linha",i+1,"Coluna:",j+1)
                        v=int(input("Digite o valor para essa posição: "))
                        print("***")
                        matriz3[i].append(v)      
                matriz=matriz3                                
            elif tamanho==4:
                for i in range (4):
                    for j in range(4):
                        print("Linha",i+1,"Coluna:",j+1)
                        v=int(input("Digite o valor para essa posição: "))
                        print("***")
                        matriz4[i].append(v)
                matriz=matriz4
        print("A matriz é: ")
        for i in range(tamanho):
            print(matriz[i])
        print("-"*20)              
        if Menu==1 or 3:
            if tamanho==1:
                Determinante=matriz[0]
            elif tamanho==2:
                Determinante=Determinante2x2(matriz,Determinante)
            elif tamanho==3:
                Determinante=Determinante3x3(matriz,Determinante)
            else:
                Determinante=Determinante4x4(matriz,Determinante)
            if Menu==1:
                print("A determinante dessa matriz é:",Determinante)
                print("-"*20)
            if Menu==3:
                if Determinante==0:
                    print("Essa matriz não tem inversa")
                    print("-"*20)
                else:
                    if tamanho==1:
                        matrizinversa=MatrizInversa1x1(matrizinversa1,matriz,Determinante)
                    if tamanho==2:
                        matrizinversa=MatrizInversa2x2(matrizinversa2,matriz,Determinante)
                    if tamanho==3:
                        matrizinversa=MatrizInversa3x3(matrizinversa3,matriz,Determinante)
                    if tamanho==4:
                        matrizinversa=MatrizInversa4x4(matrizinversa4,matriz,Determinante)
                    print("A matriz inversa é: ")
                    for i in range(tamanho):
                        print(matrizinversa[i])
                    print("-"*20)
    elif Menu==2:
          
        Rn=(int(input("Digite o valor de n do Rn: ")))

        if Rn == 0:
            print("Valor inválido!")
        elif Rn == 1: 
            while a == 0:
                 a=(int(input("Digite o valor da base A: ")))
            vetorA[0][0] = a
            while b == 0:
                b=(int(input("Digite o valor da base B: ")))
            vetorB[0][0] = b
            if vetorB[0][0]>=0:
                matriz_inversa[0][0] = (1 / vetorB[0][0])
            else:
                matriz_inversa[0][0] = (-1 / vetorB[0][0])

                matriz_mudança_base[0][0] = (matriz_inversa[0][0]*vetorA[0][0])
        
            print(matriz_mudança_base[0][0])
        elif Rn == 2:
            for i in range(0,Rn):
                for j in range(0,Rn):
                    a=(int(input(f"Digite o valor da {j + 1}ª linha e {i + 1}ª coluna da base A: ")))
                    vetorA[i][j] = a
                    a = 0
                    b=(int(input(f"Digite o valor da {j + 1}ª linha e {i + 1}ª coluna da base B: ")))
                    vetorB[i][j] = b
                    b = 0
            DeterminanteA=(vetorA[0][0]*vetorA[1][1])-(vetorA[0][1]*vetorA[1][0])
            DeterminanteB=(vetorB[0][0]*vetorB[1][1])-(vetorB[0][1]*vetorB[1][0])
            if (DeterminanteA or DeterminanteB) == 0:
                print("Algum dos dois vetores não é uma base linear!")
            else:    
                matriz_inversa[0][0]=round(vetorB[1][1]/DeterminanteB,2)
                matriz_inversa[0][1]=round(-vetorB[0][1]/DeterminanteB,2)
                matriz_inversa[1][0]=round(-vetorB[1][0]/DeterminanteB,2)
                matriz_inversa[1][1]=round(vetorB[0][0]/DeterminanteB,2)
    
            matriz_mudança_base[0][0]= round((matriz_inversa[0][0]*vetorA[0][0]) + (matriz_inversa[0][1]*vetorA[1][0]),2)
            matriz_mudança_base[0][1]= round((matriz_inversa[0][0]*vetorA[0][1]) + (matriz_inversa[0][1]*vetorA[1][1]),2)
            matriz_mudança_base[1][0]= round((matriz_inversa[1][0]*vetorA[0][0]) + (matriz_inversa[1][1]*vetorA[1][0]),2)
            matriz_mudança_base[1][1]= round((matriz_inversa[1][0]*vetorA[0][1]) + (matriz_inversa[1][1]*vetorA[1][1]),2)
        elif Rn == 3:
            for i in range(0,Rn):
                for j in range(0,Rn):
                    a=(int(input(f"Digite o valor da {j + 1}ª linha e {i + 1}ª coluna da base A: ")))
                    vetorA[i][j] = a
                    a = 0
                    b=(int(input(f"Digite o valor da {j + 1}ª linha e {i + 1}ª coluna da base B: ")))
                    vetorB[i][j] = b
                    b = 0
            diagonalPositivaA=(vetorA[0][0]*vetorA[1][1]*vetorA[2][2])+(vetorA[2][0]*vetorA[0][1]*vetorA[1][2])+(vetorA[1][0]*vetorA[2][1]*vetorA[0][2])
            diagonalNegativaA=(vetorA[2][2]*vetorA[0][1]*vetorA[1][0])+(vetorA[0][2]*vetorA[1][1]*vetorA[2][0])+(vetorA[1][2]*vetorA[2][1]*vetorA[0][0])
            DeterminanteA=diagonalPositivaA-diagonalNegativaA
            diagonalPositivaB=(vetorB[0][0]*vetorB[1][1]*vetorB[2][2])+(vetorB[2][0]*vetorB[0][1]*vetorB[1][2])+(vetorB[1][0]*vetorB[2][1]*vetorB[0][2])
            diagonalNegativaB=(vetorB[2][2]*vetorB[0][1]*vetorB[1][0])+(vetorB[0][2]*vetorB[1][1]*vetorB[2][0])+(vetorB[1][2]*vetorB[2][1]*vetorB[0][0])
            DeterminanteB=diagonalPositivaB-diagonalNegativaB
            if (DeterminanteA or DeterminanteB) == 0:
                print("Algum dos dois vetores não é uma base linear!")
            else:
                matriz_inversa[0][0]=round(((vetorB[1][1]*vetorB[2][2])-(vetorB[1][2]*vetorB[2][1]))/DeterminanteB,2)
                matriz_inversa[0][1]=round(-((vetorB[0][1]*vetorB[2][2])-(vetorB[0][2]*vetorB[2][1]))/DeterminanteB,2)
                matriz_inversa[0][2]=round(((vetorB[0][1]*vetorB[1][2])-(vetorB[0][2]*vetorB[1][1]))/DeterminanteB,2)
                matriz_inversa[1][0]=round(-((vetorB[1][0]*vetorB[2][2])-(vetorB[1][2]*vetorB[2][0]))/DeterminanteB,2)
                matriz_inversa[1][1]=round(((vetorB[0][0]*vetorB[2][2])-(vetorB[0][2]*vetorB[2][0]))/DeterminanteB,2)
                matriz_inversa[1][2]=round(-((vetorB[0][0]*vetorB[1][2])-(vetorB[0][2]*vetorB[1][0]))/DeterminanteB,2)
                matriz_inversa[2][0]=round(((vetorB[1][0]*vetorB[2][1])-(vetorB[1][1]*vetorB[2][0]))/DeterminanteB,2)
                matriz_inversa[2][1]=round(-((vetorB[0][0]*vetorB[2][1])-(vetorB[0][1]*vetorB[2][0]))/DeterminanteB,2)
                matriz_inversa[2][2]=round(((vetorB[0][0]*vetorB[1][1])-(vetorB[0][1]*vetorB[1][0]))/DeterminanteB,2)
            matriz_mudança_base[0][0]= round((matriz_inversa[0][0]*vetorA[0][0]) + (matriz_inversa[0][1]*vetorA[1][0]) + (matriz_inversa[0][2]*vetorA[2][0]),2)
            matriz_mudança_base[0][1]= round((matriz_inversa[0][0]*vetorA[0][1]) + (matriz_inversa[0][1]*vetorA[1][1]) + (matriz_inversa[0][2]*vetorA[2][1]),2)
            matriz_mudança_base[0][2]= round((matriz_inversa[0][0]*vetorA[0][2]) + (matriz_inversa[0][1]*vetorA[1][2]) + (matriz_inversa[0][2]*vetorA[2][2]),2)
            matriz_mudança_base[1][0]= round((matriz_inversa[1][0]*vetorA[0][0]) + (matriz_inversa[1][1]*vetorA[1][0]) + (matriz_inversa[1][2]*vetorA[2][0]),2)
            matriz_mudança_base[1][1]= round((matriz_inversa[1][0]*vetorA[0][1]) + (matriz_inversa[1][1]*vetorA[1][1]) + (matriz_inversa[1][2]*vetorA[2][1]),2)
            matriz_mudança_base[1][2]= round((matriz_inversa[1][0]*vetorA[0][2]) + (matriz_inversa[1][1]*vetorA[1][2]) + (matriz_inversa[1][2]*vetorA[2][2]),2)
            matriz_mudança_base[2][0]= round((matriz_inversa[2][0]*vetorA[0][0]) + (matriz_inversa[2][1]*vetorA[1][0]) + (matriz_inversa[2][2]*vetorA[2][0]),2)    
            matriz_mudança_base[2][1]= round((matriz_inversa[2][0]*vetorA[0][1]) + (matriz_inversa[2][1]*vetorA[1][1]) + (matriz_inversa[2][2]*vetorA[2][1]),2)    
            matriz_mudança_base[2][2]= round((matriz_inversa[2][0]*vetorA[0][2]) + (matriz_inversa[2][1]*vetorA[1][2]) + (matriz_inversa[2][2]*vetorA[2][2]),2)    
        elif Rn == 4:
            for i in range(0,Rn):
                for j in range(0,Rn):
                    a=(int(input(f"Digite o valor da {j + 1}ª linha e {i + 1}ª coluna da base A: ")))
                    vetorA[i][j] = a
                    a = 0
                    b=(int(input(f"Digite o valor da {j + 1}ª linha e {i + 1}ª coluna da base B: ")))
                    vetorB[i][j] = b
                    b = 0 
            diagonalPositivaA1=(vetorA[1][1]*vetorA[2][2]*vetorA[3][3])+(vetorA[3][1]*vetorA[1][2]*vetorA[2][3])+(vetorA[2][1]*vetorA[3][2]*vetorA[1][3])
            diagonalNegativaA1=(vetorA[3][3]*vetorA[1][2]*vetorA[2][1])+(vetorA[1][3]*vetorA[2][2]*vetorA[3][1])+(vetorA[2][3]*vetorA[3][2]*vetorA[1][1])
            CofatorA1=diagonalPositivaA1-diagonalNegativaA1
            diagonalPositivaA2=(vetorA[0][1]*vetorA[2][2]*vetorA[3][3])+(vetorA[3][1]*vetorA[0][2]*vetorA[2][3])+(vetorA[2][1]*vetorA[3][2]*vetorA[0][3])
            diagonalNegativaA2=(vetorA[3][3]*vetorA[0][2]*vetorA[2][1])+(vetorA[0][3]*vetorA[2][2]*vetorA[3][1])+(vetorA[2][3]*vetorA[3][2]*vetorA[0][1])
            CofatorA2=diagonalPositivaA2-diagonalNegativaA2
            diagonalPositivaA3=(vetorA[0][1]*vetorA[1][2]*vetorA[3][3])+(vetorA[3][1]*vetorA[0][2]*vetorA[1][3])+(vetorA[1][1]*vetorA[3][2]*vetorA[0][3])
            diagonalNegativaA3=(vetorA[3][3]*vetorA[0][2]*vetorA[1][1])+(vetorA[0][3]*vetorA[1][2]*vetorA[3][1])+(vetorA[1][3]*vetorA[3][2]*vetorA[0][1])
            CofatorA3=diagonalPositivaA3-diagonalNegativaA3
            diagonalPositivaA4=(vetorA[0][1]*vetorA[1][2]*vetorA[2][3])+(vetorA[2][1]*vetorA[0][2]*vetorA[1][3])+(vetorA[1][1]*vetorA[2][2]*vetorA[0][3])
            diagonalNegativaA4=(vetorA[2][3]*vetorA[0][2]*vetorA[1][1])+(vetorA[0][3]*vetorA[1][2]*vetorA[2][1])+(vetorA[1][3]*vetorA[2][2]*vetorA[0][1])
            CofatorA4=diagonalPositivaA4-diagonalNegativaA4
            DeterminanteA=(vetorA[0][0]*CofatorA1)-(vetorA[1][0]*CofatorA2)+(vetorA[2][0]*CofatorA3)-(vetorA[3][0]*CofatorA4)
            diagonalPositivaB1=(vetorB[1][1]*vetorB[2][2]*vetorB[3][3])+(vetorB[3][1]*vetorB[1][2]*vetorB[2][3])+(vetorB[2][1]*vetorB[3][2]*vetorB[1][3])
            diagonalNegativaB1=(vetorB[3][3]*vetorB[1][2]*vetorB[2][1])+(vetorB[1][3]*vetorB[2][2]*vetorB[3][1])+(vetorB[2][3]*vetorB[3][2]*vetorB[1][1])
            CofatorB1=diagonalPositivaB1-diagonalNegativaB1
            diagonalPositivaB2=(vetorB[0][1]*vetorB[2][2]*vetorB[3][3])+(vetorB[3][1]*vetorB[0][2]*vetorB[2][3])+(vetorB[2][1]*vetorB[3][2]*vetorB[0][3])
            diagonalNegativaB2=(vetorB[3][3]*vetorB[0][2]*vetorB[2][1])+(vetorB[0][3]*vetorB[2][2]*vetorB[3][1])+(vetorB[2][3]*vetorB[3][2]*vetorB[0][1])
            CofatorB2=diagonalPositivaB2-diagonalNegativaB2
            diagonalPositivaB3=(vetorB[0][1]*vetorB[1][2]*vetorB[3][3])+(vetorB[3][1]*vetorB[0][2]*vetorB[1][3])+(vetorB[1][1]*vetorB[3][2]*vetorB[0][3])
            diagonalNegativaB3=(vetorB[3][3]*vetorB[0][2]*vetorB[1][1])+(vetorB[0][3]*vetorB[1][2]*vetorB[3][1])+(vetorB[1][3]*vetorB[3][2]*vetorB[0][1])
            CofatorB3=diagonalPositivaB3-diagonalNegativaB3
            diagonalPositivaB4=(vetorB[0][1]*vetorB[1][2]*vetorB[2][3])+(vetorB[2][1]*vetorB[0][2]*vetorB[1][3])+(vetorB[1][1]*vetorB[2][2]*vetorB[0][3])
            diagonalNegativaB4=(vetorB[2][3]*vetorB[0][2]*vetorB[1][1])+(vetorB[0][3]*vetorB[1][2]*vetorB[2][1])+(vetorB[1][3]*vetorB[2][2]*vetorB[0][1])
            CofatorB4=diagonalPositivaB4-diagonalNegativaB4
            DeterminanteB=(vetorB[0][0]*CofatorB1)-(vetorB[1][0]*CofatorB2)+(vetorB[2][0]*CofatorB3)-(vetorB[3][0]*CofatorB4)
            if (DeterminanteA or DeterminanteB) == 0:
                print("Algum dos dois vetores não é uma base linear!")
            else:
                matriz_inversa[0][0]=round(((vetorB[3][1]*vetorB[1][2]*vetorB[2][3])+(vetorB[1][1]*vetorB[2][2]*vetorB[3][3])+(vetorB[2][1]*vetorB[3][2]*vetorB[1][3])-(vetorB[3][3]*vetorB[1][2]*vetorB[2][1])-(vetorB[1][3]*vetorB[2][2]*vetorB[3][1])-(vetorB[2][3]*vetorB[3][2]*vetorB[1][1]))/DeterminanteB,2)
                matriz_inversa[1][0]=-round(((vetorB[3][0]*vetorB[1][2]*vetorB[2][3])+(vetorB[1][0]*vetorB[2][2]*vetorB[3][3])+(vetorB[2][0]*vetorB[3][2]*vetorB[1][3])-(vetorB[3][3]*vetorB[1][2]*vetorB[2][0])-(vetorB[1][3]*vetorB[2][2]*vetorB[3][0])-(vetorB[2][3]*vetorB[3][2]*vetorB[1][0]))/DeterminanteB,2)
                matriz_inversa[2][0]=round(((vetorB[3][0]*vetorB[1][1]*vetorB[2][3])+(vetorB[1][0]*vetorB[2][1]*vetorB[3][3])+(vetorB[2][0]*vetorB[3][1]*vetorB[1][3])-(vetorB[3][3]*vetorB[1][1]*vetorB[2][0])-(vetorB[1][3]*vetorB[2][1]*vetorB[3][0])-(vetorB[2][3]*vetorB[3][1]*vetorB[1][0]))/DeterminanteB,2)
                matriz_inversa[3][0]=-round(((vetorB[3][0]*vetorB[1][1]*vetorB[2][2])+(vetorB[1][0]*vetorB[2][1]*vetorB[3][2])+(vetorB[2][0]*vetorB[3][1]*vetorB[1][2])-(vetorB[3][2]*vetorB[1][1]*vetorB[2][0])-(vetorB[1][2]*vetorB[2][1]*vetorB[3][0])-(vetorB[2][2]*vetorB[3][1]*vetorB[1][0]))/DeterminanteB,2)
                matriz_inversa[0][1]=-round(((vetorB[3][1]*vetorB[0][2]*vetorB[2][3])+(vetorB[0][1]*vetorB[2][2]*vetorB[3][3])+(vetorB[2][1]*vetorB[3][2]*vetorB[0][3])-(vetorB[3][3]*vetorB[0][2]*vetorB[2][1])-(vetorB[0][3]*vetorB[2][2]*vetorB[3][1])-(vetorB[2][3]*vetorB[3][2]*vetorB[0][1]))/DeterminanteB,2)
                matriz_inversa[1][1]=round(((vetorB[3][0]*vetorB[0][2]*vetorB[2][3])+(vetorB[0][0]*vetorB[2][2]*vetorB[3][3])+(vetorB[2][0]*vetorB[3][2]*vetorB[0][3])-(vetorB[3][3]*vetorB[0][2]*vetorB[2][0])-(vetorB[0][3]*vetorB[2][2]*vetorB[3][0])-(vetorB[2][3]*vetorB[3][2]*vetorB[0][0]))/DeterminanteB,2)
                matriz_inversa[2][1]=-round(((vetorB[3][0]*vetorB[0][1]*vetorB[2][3])+(vetorB[0][0]*vetorB[2][1]*vetorB[3][3])+(vetorB[2][0]*vetorB[3][1]*vetorB[0][3])-(vetorB[3][3]*vetorB[0][1]*vetorB[2][0])-(vetorB[0][3]*vetorB[2][1]*vetorB[3][0])-(vetorB[2][3]*vetorB[3][1]*vetorB[0][0]))/DeterminanteB,2)
                matriz_inversa[3][1]=round(((vetorB[3][0]*vetorB[0][1]*vetorB[2][2])+(vetorB[0][0]*vetorB[2][1]*vetorB[3][2])+(vetorB[2][0]*vetorB[3][1]*vetorB[0][2])-(vetorB[3][2]*vetorB[0][1]*vetorB[2][0])-(vetorB[0][2]*vetorB[2][1]*vetorB[3][0])-(vetorB[2][2]*vetorB[3][1]*vetorB[0][0]))/DeterminanteB,2)
                matriz_inversa[0][2]=round(((vetorB[3][1]*vetorB[0][2]*vetorB[1][3])+(vetorB[0][1]*vetorB[1][2]*vetorB[3][3])+(vetorB[1][1]*vetorB[3][2]*vetorB[0][3])-(vetorB[3][3]*vetorB[0][2]*vetorB[1][1])-(vetorB[0][3]*vetorB[1][2]*vetorB[3][1])-(vetorB[1][3]*vetorB[3][2]*vetorB[0][1]))/DeterminanteB,2)
                matriz_inversa[1][2]=-round(((vetorB[3][0]*vetorB[0][2]*vetorB[1][3])+(vetorB[0][0]*vetorB[1][2]*vetorB[3][3])+(vetorB[1][0]*vetorB[3][2]*vetorB[0][3])-(vetorB[3][3]*vetorB[0][2]*vetorB[1][0])-(vetorB[0][3]*vetorB[1][2]*vetorB[3][0])-(vetorB[1][3]*vetorB[3][2]*vetorB[0][0]))/DeterminanteB,2)
                matriz_inversa[2][2]=round(((vetorB[3][0]*vetorB[0][1]*vetorB[1][3])+(vetorB[0][0]*vetorB[1][1]*vetorB[3][3])+(vetorB[1][0]*vetorB[3][1]*vetorB[0][3])-(vetorB[3][3]*vetorB[0][1]*vetorB[1][0])-(vetorB[0][3]*vetorB[1][1]*vetorB[3][0])-(vetorB[1][3]*vetorB[3][1]*vetorB[0][0]))/DeterminanteB,2)
                matriz_inversa[3][2]=-round(((vetorB[3][0]*vetorB[0][1]*vetorB[1][2])+(vetorB[0][0]*vetorB[1][1]*vetorB[3][2])+(vetorB[1][0]*vetorB[3][1]*vetorB[0][2])-(vetorB[3][2]*vetorB[0][1]*vetorB[1][0])-(vetorB[0][2]*vetorB[1][1]*vetorB[3][0])-(vetorB[1][2]*vetorB[3][1]*vetorB[0][0]))/DeterminanteB,2)
                matriz_inversa[0][3]=-round(((vetorB[2][1]*vetorB[0][2]*vetorB[1][3])+(vetorB[0][1]*vetorB[1][2]*vetorB[2][3])+(vetorB[1][1]*vetorB[2][2]*vetorB[0][3])-(vetorB[2][3]*vetorB[0][2]*vetorB[1][1])-(vetorB[0][3]*vetorB[1][2]*vetorB[2][1])-(vetorB[1][3]*vetorB[2][2]*vetorB[0][1]))/DeterminanteB,2)
                matriz_inversa[1][3]=round(((vetorB[2][0]*vetorB[0][2]*vetorB[1][3])+(vetorB[0][0]*vetorB[1][2]*vetorB[2][3])+(vetorB[1][0]*vetorB[2][2]*vetorB[0][3])-(vetorB[2][3]*vetorB[0][2]*vetorB[1][0])-(vetorB[0][3]*vetorB[1][2]*vetorB[2][0])-(vetorB[1][3]*vetorB[2][2]*vetorB[0][0]))/DeterminanteB,2)
                matriz_inversa[2][3]=-round(((vetorB[2][0]*vetorB[0][1]*vetorB[1][3])+(vetorB[0][0]*vetorB[1][1]*vetorB[2][3])+(vetorB[1][0]*vetorB[2][1]*vetorB[0][3])-(vetorB[2][3]*vetorB[0][1]*vetorB[1][0])-(vetorB[0][3]*vetorB[1][1]*vetorB[2][0])-(vetorB[1][3]*vetorB[2][1]*vetorB[0][0]))/DeterminanteB,2)
                matriz_inversa[3][3]=round(((vetorB[2][0]*vetorB[0][1]*vetorB[1][2])+(vetorB[0][0]*vetorB[1][1]*vetorB[2][2])+(vetorB[1][0]*vetorB[2][1]*vetorB[0][2])-(vetorB[2][2]*vetorB[0][1]*vetorB[1][0])-(vetorB[0][2]*vetorB[1][1]*vetorB[2][0])-(vetorB[1][2]*vetorB[2][1]*vetorB[0][0]))/DeterminanteB,2)
            matriz_mudança_base[0][0]= round((matriz_inversa[0][0]*vetorA[0][0]) + (matriz_inversa[0][1]*vetorA[1][0]) + (matriz_inversa[0][2]*vetorA[2][0]) + (matriz_inversa[0][3]*vetorA[3][0]),2)
            matriz_mudança_base[0][1]= round((matriz_inversa[0][0]*vetorA[0][1]) + (matriz_inversa[0][1]*vetorA[1][1]) + (matriz_inversa[0][2]*vetorA[2][1]) + (matriz_inversa[0][3]*vetorA[3][1]),2)
            matriz_mudança_base[0][2]= round((matriz_inversa[0][0]*vetorA[0][2]) + (matriz_inversa[0][1]*vetorA[1][2]) + (matriz_inversa[0][2]*vetorA[2][2]) + (matriz_inversa[0][3]*vetorA[3][2]),2)
            matriz_mudança_base[0][3]= round((matriz_inversa[0][0]*vetorA[0][3]) + (matriz_inversa[0][1]*vetorA[1][3]) + (matriz_inversa[0][2]*vetorA[2][3]) + (matriz_inversa[0][3]*vetorA[3][3]),2)
            matriz_mudança_base[1][0]= round((matriz_inversa[1][0]*vetorA[0][0]) + (matriz_inversa[1][1]*vetorA[1][0]) + (matriz_inversa[1][2]*vetorA[2][0]) + (matriz_inversa[1][3]*vetorA[3][0]),2)
            matriz_mudança_base[1][1]= round((matriz_inversa[1][0]*vetorA[0][1]) + (matriz_inversa[1][1]*vetorA[1][1]) + (matriz_inversa[1][2]*vetorA[2][1]) + (matriz_inversa[1][3]*vetorA[3][1]),2)
            matriz_mudança_base[1][2]= round((matriz_inversa[1][0]*vetorA[0][2]) + (matriz_inversa[1][1]*vetorA[1][2]) + (matriz_inversa[1][2]*vetorA[2][2]) + (matriz_inversa[1][3]*vetorA[3][2]),2)
            matriz_mudança_base[1][3]= round((matriz_inversa[1][0]*vetorA[0][3]) + (matriz_inversa[1][1]*vetorA[1][3]) + (matriz_inversa[1][2]*vetorA[2][3]) + (matriz_inversa[1][3]*vetorA[3][3]),2)
            matriz_mudança_base[2][0]= round((matriz_inversa[2][0]*vetorA[0][0]) + (matriz_inversa[2][1]*vetorA[1][0]) + (matriz_inversa[2][2]*vetorA[2][0]) + (matriz_inversa[2][3]*vetorA[3][0]),2)    
            matriz_mudança_base[2][1]= round((matriz_inversa[2][0]*vetorA[0][1]) + (matriz_inversa[2][1]*vetorA[1][1]) + (matriz_inversa[2][2]*vetorA[2][1]) + (matriz_inversa[2][3]*vetorA[3][1]),2)    
            matriz_mudança_base[2][2]= round((matriz_inversa[2][0]*vetorA[0][2]) + (matriz_inversa[2][1]*vetorA[1][2]) + (matriz_inversa[2][2]*vetorA[2][2]) + (matriz_inversa[2][3]*vetorA[3][2]),2)
            matriz_mudança_base[2][3]= round((matriz_inversa[2][0]*vetorA[0][3]) + (matriz_inversa[2][1]*vetorA[1][3]) + (matriz_inversa[2][2]*vetorA[2][3]) + (matriz_inversa[2][3]*vetorA[3][3]),2)
            matriz_mudança_base[3][0]= round((matriz_inversa[3][0]*vetorA[0][0]) + (matriz_inversa[3][1]*vetorA[1][0]) + (matriz_inversa[3][2]*vetorA[2][0]) + (matriz_inversa[3][3]*vetorA[3][0]),2)
            matriz_mudança_base[3][1]= round((matriz_inversa[3][0]*vetorA[0][1]) + (matriz_inversa[3][1]*vetorA[1][1]) + (matriz_inversa[3][2]*vetorA[2][1]) + (matriz_inversa[3][3]*vetorA[3][1]),2)
            matriz_mudança_base[3][2]= round((matriz_inversa[3][0]*vetorA[0][2]) + (matriz_inversa[3][1]*vetorA[1][2]) + (matriz_inversa[3][2]*vetorA[2][2]) + (matriz_inversa[3][3]*vetorA[3][2]),2)  
            matriz_mudança_base[3][3]= round((matriz_inversa[3][0]*vetorA[0][3]) + (matriz_inversa[3][1]*vetorA[1][3]) + (matriz_inversa[3][2]*vetorA[2][3]) + (matriz_inversa[3][3]*vetorA[3][3]),2)


        print(vetorA)
        print(vetorB)
        print(matriz_inversa)
        print(matriz_mudança_base)
    else:
        print("Comando inválido")
        print("-"*20)    