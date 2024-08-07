def eat_ghost(power_pellet_active, touching_ghost):
    

    return power_pellet_active and touching_ghost

pac1= eat_ghost(True,True)

print(pac1)
def score(touching_power_pellet, touching_dot):
 
    return touching_power_pellet or touching_dot
    

pac2 =score(True,False)
print(pac2)

def lose(power_pellet_active, touching_ghost):
 
    if power_pellet_active ==False and touching_ghost == True:
        return True
    else:
       return False
            
pac3= lose(True,True)
print (pac3)