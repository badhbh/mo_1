
def find_func_min(x0, func, beta):
    mass = []

    if(func(x0) > func(x0 +beta)): 
        mass.append(x0)      
        x1 = x0 + beta
        mass.append(x1)
        print("x1 is:", x1)
        h = beta
        print("h is:", h)
    elif(func(x0) > func(x0 - beta)):
        mass.append(x0)
        x1 = x0 - beta
        mass.append(x1)
        print("x1 is:", x1)
        h = beta * -1
        print("h is:", h)
    while True:
        h *=2
        print("h change:", h)
        x1 = x0 + h
        mass.append(x1)
        print("x1 change:", x1)
        if(func(x0) > func(x1)):
            x0 = x1
            print("x0 is:", x0)
        else:            
            print("min:", mass[-3], " ", mass[-1] )
            break 






