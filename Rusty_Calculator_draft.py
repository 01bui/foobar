def isNumber(item):
    try:
        float(item)
        return 1
    except ValueError:
        pass

def answer(input):
    # your code here
    eq = input.split(' ')
    assert (len(eq) >= 3),"Not enough values in the equation."
    import operator as op
    ops = {'+':op.add, '*':op.mul}
    stack = []
    for item in eq:
        #print item
        if isNumber(item):
            stack.insert(0,item)
        else:
            num1 = float(stack.pop(1))
            num2 = float(stack.pop(0))
            ans = ops[item](num1,num2)
            stack.insert(0,ans)
            #print ans
    return str(ans)

def main():
    while 1:
        input = raw_input('Equation: ')
        ans = answer(input)
        print ans

if __name__ == '__main__':
    main()