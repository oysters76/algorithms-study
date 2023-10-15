import math 
def bestSum(n, options):

    if n == 0:
        return [] 
    
    if n < 0:
        return None 
    
    best = None 
    min = math.inf

    for option in options:
        sol = bestSum(n-option, options) 
        
        if sol == None:
            continue
        
        if len(sol) < min:
            best = sol + [option]
            min = len(sol)

    return best 

def bestSumMem(n, options, mem={}):
    if n in mem:
        return mem[n] 
    
    if n == 0:
        return [] 
    
    if n < 0:
        return None 

    best = None 
    min = math.inf 

    for option in options:
        sol = bestSumMem(n-option, options, mem) 
        
        if sol == None:
            continue 

        if len(sol) < min:
            best = sol + [option] 
            min = len(sol) 
    
    mem[n] = best 
    return mem[n]


print(bestSumMem(100, [25,1,2,5]))
