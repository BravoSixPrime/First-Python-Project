block1='       '
block2='_______'
def line1():
    print((block1+'|')*2+block1)
def line2():
    print((block2+'|')*2+block2)
block=[]
def PrintBoard(block):
    print('_'*23)
    line1()
    print('   '+str(block[0])+'   '+'|'+'   '+str(block[1])+'   '+'|'+'   '+str(block[2])+'   ')
    line2()
    line1()
    print('   '+str(block[3])+'   '+'|'+'   '+str(block[4])+'   '+'|'+'   '+str(block[5])+'   ')
    line2()
    line1()
    print('   '+str(block[6])+'   '+'|'+'   '+str(block[7])+'   '+'|'+'   '+str(block[8])+'   ')
    line2()
    print('\n')
print("Control Keys are mapped as below:")
list1=[7,8,9,4,5,6,1,2,3]
PrintBoard(list1)
my_dict={'7':0,'8':1,'9':2,'4':3,'5':4,'6':5,'1':6,'2':7,'3':8} #Mapping Keys to index
list2=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
p1=input("Enter your name player 1 (X): ")
p2=input("Enter your name player 2 (O): ")
def PlayerInput(symbol,p):
    s=input(f"Choose your position {p}  : ")
    n=my_dict[s]
    if list2[n]!=' ':
            print('Position is taken , Choose another one!')
            PlayerInput(symbol,p)
    for i in range(9):
        if i==n:
            list2[i]=symbol
        elif list2[i]==' ':
            list2[i]=' '
    return list2
i=0
def WinCondition(list2):
    list3=[0,3,6]
    for i in list3:
        if list2[i]!=' ' and (list2[i]==list2[i+1] and list2[i+1]==list2[i+2]):
            return 0
    for i in range(3):
        if list2[i]!=' ' and (list2[i]==list2[i+3] and list2[i+3]==list2[i+6]):
            return 0
    if (list2[0]!=' ' and (list2[0]==list2[4] and list2[4]==list2[8])) or (list2[2]!=' ' and (list2[2]==list2[4] and list2[4]==list2[6])):
        return 0
    return 1

while (WinCondition(list2)):
    if i%2==0:
        PlayerInput('X',p1)
        PrintBoard(list2)
    else:
        PlayerInput('O',p2)
        PrintBoard(list2)
    i+=1
    if i==9:
        break
        
if i%2==0:
    print(f"Congrats {p2}, you won!!!")
elif i==9:
    print('Its a draw!')
else:
    print(f"Congrats {p1}, you won!!!")





    
    


