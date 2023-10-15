def gridTraveller(n,m,mem={}):
    if ((n,m) in mem):
        return mem[(n,m)] 
    if n == 0 or m == 0:
        return 0 
    if n == 1 and m == 1:
        return 1 
    
    mem[(n,m)] = gridTraveller(n-1, m, mem) + gridTraveller(n, m-1, mem) 
    return mem[(n,m)]

def gridTravel(n,m,mem={}):
    stack = [(n,m)] 
    total = 0
    while len(stack) > 0:
        dim = stack.pop() 
        x, y = dim 
        
        if ((x,y) in mem):
            total += mem[(x,y)] 
            continue 
        
        if x == 0 or y == 0:
            continue  
        
        if x == 1 and y == 1:
            total += 1
        
        stack.append((x-1, y)) 
        stack.append((x, y-1)) 

    return total 

print(gridTravel(18,18))
