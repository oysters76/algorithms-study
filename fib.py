def fib(n, mem={}):
    if n in mem:
        return mem[n] 
    if n <= 2:
        return 1 
    mem[n] = fib(n-1) + fib(n-2) 
    return mem[n] 

def fib2(n,mem={}):
    total = 0 
    stack = [n] 
    while len(stack) > 0:
        n = stack.pop() 

        if n in mem:
            total += mem[n] 

        if n <= 2:
            mem[n] = 1
            total += 1 

        stack.append(n-1)
        stack.append(n-2) 
    return total


print(fib2(50))