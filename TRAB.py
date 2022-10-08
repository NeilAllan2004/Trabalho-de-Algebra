Menu=0
while Menu!=4:
    Menu=int(input("1.Determinante da matriz\n2.Mudança de base\n3.Matriz inversa\n4.Sair\nDigite qual opção você deseja: "))
    print("-"*20)
    matriz1=[]
    matriz2=[[],[]]
    matriz3=[[],[],[]]
    matriz4=[[],[],[],[]]
    matrizinversa1=[]
    matrizinversa2=[[0,0],[0,0]]
    matrizinversa3=[[0,0,0],[0,0,0],[0,0,0]]
    matrizinversa4=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    x=0
    diagonalPositiva=0
    diagonalNegativa=0
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
                Determinante=(matriz[0][0]*matriz[1][1])-(matriz[0][1]*matriz[1][0])
            elif tamanho==3:
                diagonalPositiva=(matriz[0][0]*matriz[1][1]*matriz[2][2])+(matriz[2][0]*matriz[0][1]*matriz[1][2])+(matriz[1][0]*matriz[2][1]*matriz[0][2])
                diagonalNegativa=(matriz[2][2]*matriz[0][1]*matriz[1][0])+(matriz[0][2]*matriz[1][1]*matriz[2][0])+(matriz[1][2]*matriz[2][1]*matriz[0][0])
                Determinante=diagonalPositiva-diagonalNegativa
            else:
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
            if Menu==1:
                print("A determinante dessa matriz é:",Determinante)
                print("-"*20)
            if Menu==3:
                if Determinante==0:
                    print("Essa matriz não tem inversa")
                    print("-"*20)
                else:
                    if tamanho==1:
                        if matriz[0]>=0:
                            matrizinversa1.append(1/matriz[0])
                        else:
                            matrizinversa1.append(-1/matriz[0])
                        matrizinversa=matrizinversa1
                    if tamanho==2:
                        matrizinversa2[0][0]=matriz[1][1]/Determinante
                        matrizinversa2[0][1]=-matriz[0][1]/Determinante
                        matrizinversa2[1][0]=-matriz[1][0]/Determinante
                        matrizinversa2[1][1]=matriz[0][0]/Determinante
                        matrizinversa=matrizinversa2
                    if tamanho==3:
                        matrizinversa3[0][0]=((matriz[1][1]*matriz[2][2])-(matriz[1][2]*matriz[2][1]))/Determinante
                        matrizinversa3[0][1]=-((matriz[0][1]*matriz[2][2])-(matriz[0][2]*matriz[2][1]))/Determinante
                        matrizinversa3[0][2]=((matriz[0][1]*matriz[1][2])-(matriz[0][2]*matriz[1][1]))/Determinante
                        matrizinversa3[1][0]=-((matriz[1][0]*matriz[2][2])-(matriz[1][2]*matriz[2][0]))/Determinante
                        matrizinversa3[1][1]=((matriz[0][0]*matriz[2][2])-(matriz[0][2]*matriz[2][0]))/Determinante
                        matrizinversa3[1][2]=-((matriz[0][0]*matriz[1][2])-(matriz[0][2]*matriz[1][0]))/Determinante
                        matrizinversa3[2][0]=((matriz[1][0]*matriz[2][1])-(matriz[1][1]*matriz[2][0]))/Determinante
                        matrizinversa3[2][1]=-((matriz[0][0]*matriz[2][1])-(matriz[0][1]*matriz[2][0]))/Determinante
                        matrizinversa3[2][2]=((matriz[0][0]*matriz[1][1])-(matriz[0][1]*matriz[1][0]))/Determinante
                        matrizinversa=matrizinversa3
                    if tamanho==4:
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
                        matrizinversa=matrizinversa4
                    print("A matriz inversa é: ")
                    for i in range(tamanho):
                        print(matrizinversa[i])
                    print("-"*20)
    elif Menu==2:
        print("yes")
    else:
        print("Comando inválido")
        print("-"*20)    