import copy
def newMat(m,x):
    newSize=len(m)-1
    returnable=[None]*newSize
    crunch=[None]*3
    for i in range(len(returnable)):
        returnable[i]=[None]*newSize
    for i in range(newSize):
        for j in range(newSize):
            if(j>=x):
                k=j+1
                
            else:
                k=j
            returnable[i][j]=m[i+1][k]
            crunch[0]=returnable
            crunch[1]=m[0][x]
            crunch[2]=x
    return(crunch)
            
    
def recDeter(m,el,shift):
    print('displacement')
    print(shift)
    for i in m:
        print(i)
    if(len(m)==2):
        print('result')
        print(el*(m[0][0]*m[1][1]-m[1][0]*m[0][1]))
        return(el*(m[0][0]*m[1][1]-m[1][0]*m[0][1]))
    else:
        result=0
        for i in range(len(m)):
            temp=newMat(m,i)
            temp2=recDeter(temp[0],temp[1],shift+1)
            print(temp2)
            if((i+shift)%2==1):
                result-=temp2
            else:  
                result+=temp2
        return(result)
    
    
size=0
size=int(input("Размер:"))
if(size<2):
    print("Так низзя")
    exit()
matrix=[None]*size
potential=[None]*size
deltaMatrix=[None]*size
deltak=[None]*size


for i in range(len(matrix)):
    matrix[i]=[None]*size
    deltaMatrix[i]=[None]*size
    potential[i]=float(input("E"+str(i+1)+":"))
for i in range(size):
    for j in range(size):
        matrix[i][j]=int(input("Элемент["+str(i+1)+"]["+str(j+1)+"]"))


if(size==2):
    mainDeter=recDeter(matrix,1,0)
else:
    mainDeter=recDeter(matrix,matrix[0][0],0)    
print("Главный детерминант"+str(mainDeter))


for k in range(size):
    deltaMatrix=copy.deepcopy(matrix)
    for i in range(size):
        for j in range(size):
            if(j==k):
                deltaMatrix[i][j]=potential[i]
    print("Определение матрицы")
    for i in deltaMatrix:
        print(i)
    if(size==2):
        deltak[k]=recDeter(deltaMatrix,1,0)
    else:
        deltak[k]=recDeter(deltaMatrix,deltaMatrix[0][0],0)
    print("Минорный детерминант"+str(deltak[k]))
    print("Ток"+str(k+1)+":"+str(deltak[k]/mainDeter))
        
    

