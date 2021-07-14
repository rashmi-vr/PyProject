import random

def GameWin (comp, you):
    if comp==you:
        return None
    
    elif comp=='s':
        if you=='w':
            return False
        if you=='g':
            return True

    elif comp=='w':
        if you=='s':
            return True
        if you=='g':
            return False
    
    elif comp=='g':
        if you=='s':
            return False
        if you=='w':
            return True

print("Comp Turn: Snake(s), Water(w), Gun(g)? ")
randvalue = random.randint(1,3)
if randvalue == 1:
    comp = "s"
elif randvalue == 2:
    comp = "w"
elif randvalue == 3:
    comp = "g"


you = input("Your Turn: Snake(s), Water(w), Gun(g)? ")

print (f"Comp chose {comp}")
print (f"You chose {you}")

a = GameWin(comp,you)
if a==None:
    print ("This is a tie!")
elif a:
    print ("You win!")
else:
    print("You lose :-(")





