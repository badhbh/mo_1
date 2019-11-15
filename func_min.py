
def find_func_min(x0, func, beta):
    if(func(x0) > func(x0 +beta)):       
        x1 = x0 + beta
        h = beta
    
    elif(func(x0) > func(x0 - beta)):
        x1 = x0 - beta
        h = beta * -1
    while True:
        h *=h
        x1 = x0 + h
        if(func(x0) > func(x1)):
            x0 = x1
        else:
            print(x0, x1)
            break 






