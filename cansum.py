def canSum(n, options):
    if n == 0:
        return True 
    if n < 0:
        return False 
    
    can = False
    for option in options:
        can = can or canSum(n-option, options)
    return can

def canSumMemo(n, options, mem={}):
    if n in mem:
        return mem[n] 
    if n == 0:
        return True 
    if n < 0:
        return False 
    
    for option in options:
        mem[n] = canSumMemo(n-option, options, mem)
        return mem[n]
    
def canSumIter(n, options):
    stack = [n] 
    can = False
    while len(stack) > 0:
        n = stack.pop() 
        if n == 0:
            return True
        if n < 0:
            can = can or False 
            continue

        for option in options:
            stack.append(n-option)  
    return can

            

print(canSumMemo(7,[7,14]))