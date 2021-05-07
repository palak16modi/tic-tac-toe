from functions import *#or write import functions, but in this case only file is imported not functions.so use functins.check_row to call the function
a=['1','2','3']
b=['4','5','6']
c=['7','8','9']
flag=0
print (a,'\n',b,'\n',c)
for i in range(9):
    if i%2==0:
        print ("i=",i)
        player1(a,b,c)
        k='X'
    if i%2!=0:
        print( "i=",i)
        player2(a,b,c)
        k='O'
    print (a,'\n',b,'\n',c)
    if check_col(a,b,c,k) or check_row(a,b,c,k) or check_dia(a,b,c,k):
        flag=1
        break
if(flag==0):
    print("its a tie")
if i==9:
    print ("its a tie")



    
