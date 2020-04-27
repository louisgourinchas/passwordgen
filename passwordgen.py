import random

def simplegen(n):
    pswd = ""
    for i in range (n):
        mylist = list(random.randint(0,3))
        pswd = pswd + random.choice(mylist)
    print("generated password: " + pswd)

def norepgen(n):
    lastlist = -1
    pswd = ""
    for i in range (n):
        x = random.randint(0,3)
        while(x==lastlist):
            x = random.randint(0,3)
        mylist = list(x)
        pswd = pswd + random.choice(mylist)
        lastlist = x
    print("generated password: " + pswd)
    
def list(i):
    switcher={
        0:('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'),
        1:('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'),
        2:('0','1','2','3','4','5','6','7','8','9'),
        3:('&','-','_','!','?','=','#','/','\\','$','£','%','*','µ','§')
        }
    return switcher.get(i,"you somehow failed")
