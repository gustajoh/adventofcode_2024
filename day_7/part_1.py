import math

def main():
    ans = []
    terms = []
    
    with open('input.txt') as file:
        for line in file:
            eq = line.split(":")
            ans.append(int(eq[0]))
            terms.append(eq[1].strip().split(" "))
    res = checkEquations(ans, terms)
    print(res)

def checkEquations(ans, terms):
    res = 0
    for i in range(len(ans)):
        ops = 2**(len(terms[i])-1)-1
        length = len("{0:b}".format(ops))
        while ops > -1:
            op_list = list("{0:b}".format(ops).zfill(length))
            if evaluate(terms[i], op_list) == ans[i]:
                res += ans[i]
                break
            ops -= 1           
    return res

def evaluate(terms, ops):
    res = int(terms[0])
    for i in range(len(ops)):
        if ops[i] == "0":
            res *= int(terms[i + 1])
        elif ops[i] == "1":
            res += int(terms[i + 1])
    return res

if __name__ == "__main__":
       main()