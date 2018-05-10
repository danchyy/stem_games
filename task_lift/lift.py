

def get_solution(string):
    zeros = int(string)
    ans = (2*5)**zeros
    anss = []
    for i in range(10):
        anss += str(ans + i)

    return ' '.join(anss)
