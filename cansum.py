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

print(canSum(10,[7,14]))