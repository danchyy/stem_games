from math import sqrt

modulo = int(1000000007)
mem = [0, 1, 1]  
    
def power(base, exp):
   """ Fast power calculation using repeated squaring """
   if exp < 0:
       return 1 / power(base, -exp)
   ans = 1
   while exp:
       if exp & 1:
           ans = (ans%modulo * base%modulo)%modulo
       exp >>= 1
       base = (base%modulo * base%modulo)%modulo
   return ans

def fibs(n):
	if n < len(mem):
		return mem[n]
	
	for f in range(len(mem), n+1):                                                                                      
		mem.append((mem[-1]%modulo + mem[-2]%modulo)%modulo)                                                                         
	return mem[n]    
    
def modulo_multiplicative_inverse(A):
    return power(A, modulo-2)
    
def f(k):
    n = 4*k-1
    a1 = power(1+sqrt(5),n)
    a2 = power(1-sqrt(5),n)
    a3 = modulo_multiplicative_inverse(power(2,n)*sqrt(5))  
    print(a1,a2,a3)  
    return ((a1 - a2)*a3)%modulo

    
def SubFib(end):
    k = 1
    summ = int(0)
    cur = fibs(4*k-1)
    while k <= end:
        #print("n =",n)
        #print(cur)
        summ = (summ + cur)%modulo
        k += 1
        cur = fibs(4*k-1)
    return int(summ)

def get_solution(N):
    return SubFib(int(N))

print(get_solution("1000000000000000000"))
#print(fast_pow(6,18,modulo))
#print(power(6,18))

#print(fibs(13))
