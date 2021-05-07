def check_col(a,b,c,k):
    for i in range(3):
        if a[i]==b[i]==c[i]:
            print (k,'winner')
            return 1
            break
def check_row(a,b,c,k):
    for i in range(1):
        if a[i]==a[i+1]==a[i+2]:
            print (k,'winner')
            return 1
            break
        elif b[i]==b[i+1]==b[i+2]:
            print (k,'winner')
            return 1
            break
        elif c[i]==c[i+1]==c[i+2]:
            print (k,'winner')
            return 1
            break
def check_dia(a,b,c,k):
    if a[0]==b[1]==c[2]:
        print (k,'winner')
        return 1
    elif a[2]==b[1]==c[0]:
        print (k,'winner')
        return 1
def check_loc(a,b,c,k):
    t=0
    #t=input("enter location")
    try:
        t=int(input("enter location"))
        print ("t=",t)
    except NameError:
        #t=0
        print ("invalid")
        check_loc(a,b,c,k)
    if t<1 or t>9:
        print ("invalid location. try again!!")
        check_loc(a,b,c,k)
    else:
        if t<4 and t>0:
            if a[t-1]=='X' or a[t-1]=='O':
                print ("that location is already taken. try again!!")
                check_loc(a,b,c,k)
            else:
                a[t-1]=k
        if t<7 and t>3:
            if b[t-4]=='X' or b[t-4]=='O':
                print ("that location is already taken. try again!!")
                check_loc(a,b,c,k)
            else:
                b[t-4]=k
        if t<10 and t>6:
            if c[t-7]=='X' or c[t-7]=='O':
                print ("that location is already taken. try again!!")
                check_loc(a,b,c,k)
            else:
                c[t-7]=k


def player1(a,b,c):
    k='X'
    print ("in player1")
    check_loc(a,b,c,k)

def player2(a,b,c):
    print ("in player2")
    k='O'
    check_loc(a,b,c,k)
    
    
    
    
