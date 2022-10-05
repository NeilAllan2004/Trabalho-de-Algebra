Menu=0
while Menu!=4:
    Menu=int(input("1.Determinante da matriz\n2.Mudança de base\n3.Matriz inversa\n4.Sair\nDigite qual opção você deseja: "))
    print("-"*20)
    matriz1=[]
    matriz2=[[],[]]
    matriz3=[[],[],[]]
    matriz4=[[],[],[],[]]
    x=0
    diagonalPositiva=0
    diagonalNegativa=0        
    if Menu==4:
        print("Programa encerrado")
        print("-"*20)
    elif Menu==1 or Menu==2 or Menu==3:
        while x==0:
            Random=int(input("1.Matriz aleatória\n2.Matriz escrita manualmente\nDigite qual opção você deseja: "))
            print("-"*20)
            if Random==1 or Random==2:
                x=1
            else:
                print("Comando inválido")
                print("-"*20)
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
            print("A matriz é:",matriz)
            print("-"*20)  
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
                v=int(input("Digite um valor: "))
                matriz1.append(v)
                matriz=matriz1
            elif tamanho==2:
                for i in range (2):
                    for j in range(2):
                        v=int(input("Digite um valor: "))
                        matriz2[i].append(v)    
                matriz=matriz2                                                    
            elif tamanho==3:
                for i in range (3):
                    for j in range(3):
                        v=int(input("Digite um valor: "))
                        matriz3[i].append(v)      
                matriz=matriz3                                
            elif tamanho==4:
                for i in range (4):
                    for j in range(4):
                        v=int(input("Digite um valor: "))
                        matriz4[i].append(v)
                matriz=matriz4
            print("A matriz é:",matriz)
            print("-"*20)              
        if Menu==1:
            if tamanho==1:
                Determinante=matriz[0]
            elif tamanho==2:
                Determinante=(matriz[0][0]*matriz[1][1])-(matriz[0][1]*matriz[1][0])
            elif tamanho==3:
                diagonalPositiva=(matriz[0][0]*matriz[1][1]*matriz[2][2])+(matriz[2][0]*matriz[0][1]*matriz[1][2])+(matriz[1][0]*matriz[2][1]*matriz[0][2])
                diagonalNegativa=(matriz[2][2]*matriz[0][1]*matriz[1][0])+(matriz[0][2]*matriz[1][1]*matriz[2][0])+(matriz[1][2]*matriz[2][1]*matriz[0][0])
                Determinante=diagonalPositiva-diagonalNegativa
            elif tamanho==4:
                print("yes")
                
            print("A determinante dessa matriz é:",Determinante)
            print("-"*20)
        if Menu==3:
            print("yes")

    else:
        print("Comando inválido")
        print("-"*20)       