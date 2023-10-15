
def howSum(n, options):
    if n == 0:
        return [] 
    if n < 0:
        return None 

    for option in options:
        arr = howSum(n-option, options)
        if (arr == None):
            return None 
        return arr + [option] 
    
    return None

def howSumMemo(n, options, mem={}):
    if n in mem:
        return mem[n] 
    if n == 0:
        return []
    if n < 0:
        return None 
    
    for option in options:
        arr = howSumMemo(n-option, options, mem) 
        if arr != None:
            mem[n] = arr + [option]
            return mem[n] 
        
    mem[n] = None 
    return mem[n]

print(howSum(8,[1]))
print(howSumMemo(300, [17,20]))
    