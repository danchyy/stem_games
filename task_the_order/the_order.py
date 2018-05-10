import math

def nthperm(word, n):
    perm = []
    while word != []:
        f = math.factorial(len(word)-1)
        i = int(math.floor(n/f)) 
        n %= f
        perm.append(word[i])
        word = word[:i] + word[i+1:]
    return "".join(perm)
    
def get_solution(word):
    string = word.split(" ")[0]
    index = int(word.split(" ")[1])
    return(nthperm(list(string),index))

